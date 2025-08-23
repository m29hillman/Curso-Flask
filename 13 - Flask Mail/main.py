"""
Arquivo principal da aplicação Flask.

Define as rotas, manipuladores de erro e a inicialização da aplicação.
Este projeto utiliza o padrão Factory para criar a aplicação, facilitando testes,
modularidade e diferentes configurações (ex: desenvolvimento, produção).
"""

# Importações de bibliotecas padrão
from datetime import datetime

# Importações de pacotes de terceiros (Flask e extensões)
from flask import render_template, session, redirect, url_for, flash, current_app

# Importações locais da aplicação
from app import create_app, db
from app.models import User, Role, NameForm
from app.email import send_email  # Função para envio de e-mails (notificações)

# Cria a instância da aplicação Flask utilizando a função factory.
# O padrão Factory evita importações circulares e permite múltiplas instâncias/configurações.
app = create_app('development')

# Rota principal da aplicação ('/'), aceita métodos GET e POST.
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Rota principal que renderiza a página inicial e processa o formulário de nome.

    Se o formulário for submetido, verifica se o usuário já existe.
    - Se for um novo usuário, ele é adicionado ao banco de dados e uma
      notificação por e-mail é enviada ao administrador.
    - Se o usuário já existir, uma mensagem informativa é exibida.

    Utiliza a sessão para lembrar o nome do usuário e se ele já era conhecido.
    O padrão Post/Redirect/Get é utilizado para evitar reenvio de formulários.
    """
    form = NameForm()
    
    # Valida o formulário: True se foi submetido e passou nos validadores.
    if form.validate_on_submit():
        # Consulta o banco de dados por um usuário com o nome informado.
        user = User.query.filter_by(username=form.name.data).first()
        
        # Se o usuário não existe, cadastra e envia e-mail de notificação.
        if user is None:
            flash('Novo nome cadastrado!')
            # Envia e-mail ao administrador informando novo cadastro.
            send_email(app, 
                       'Novo usuário ' + form.name.data, 
                       ['m29hillman@gmail.com'], 
                       "Obrigado por se cadastrar no nosso site!", 
                       None)
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False  # Marca como usuário novo
        else:
            # Usuário já existe, apenas informa.
            flash('Nome existente!')
            session['known'] = True  # Marca como usuário conhecido
            
        # Salva o nome na sessão para uso futuro.
        session['name'] = form.name.data
        form.name.data = ''  # Limpa o campo do formulário
        
        # Redireciona o usuário para a mesma rota ('index') usando uma requisição GET.
        # Este é o padrão Post/Redirect/Get, que previne o reenvio de formulários
        # caso o usuário atualize a página após uma submissão POST.
        return redirect(url_for('index'))
        
    # Se a requisição for GET (ou se o formulário não for válido), renderiza o template.
    # Passa as variáveis para o template para que possam ser usadas no HTML.
    return render_template('index.html', 
                           form=form, 
                           name=session.get('name'), 
                           known=session.get('known', False),
                           current_time=datetime.utcnow())

# O decorator @app.errorhandler registra uma função para ser chamada quando um erro HTTP específico ocorre.
# Neste caso, o erro 404 (Página Não Encontrada).
@app.errorhandler(404)
def page_not_found(e):
    """Renderiza a página de erro 404 personalizada."""
    # Retorna o template '404.html' e o código de status 404.
    return render_template('404.html'), 404

# Registra um manipulador para o erro 500 (Erro Interno do Servidor).
# Isso captura exceções não tratadas na aplicação.
@app.errorhandler(500)
def internal_server_error(e):
    """Renderiza a página de erro 500 personalizada."""
    # Retorna o template '500.html' e o código de status 500.
    return render_template('500.html'), 500

# Bloco de execução principal: só roda quando o script é executado diretamente.
if __name__ == "__main__":
    # Inicia o servidor de desenvolvimento integrado do Flask.
    # ATENÇÃO: Nunca use o servidor de desenvolvimento em produção.
    app.run(
        host='0.0.0.0',  # Torna o servidor acessível a partir de qualquer IP na rede.
        port=5000,       # Define a porta em que o servidor irá escutar.
        debug=True,      # Ativa o modo de depuração para recarregamento automático e debugger interativo.
        threaded=True    # Permite que o servidor processe múltiplas requisições simultaneamente.
    )