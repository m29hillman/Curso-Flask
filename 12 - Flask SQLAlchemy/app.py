# Importações de pacotes e módulos necessários.
# render_template: Para renderizar arquivos HTML.
# session: Para armazenar dados entre requisições de um mesmo usuário.
# redirect, url_for: Para criar redirecionamentos.
# flash: Para exibir mensagens temporárias ao usuário.
from flask import render_template, session, redirect, url_for, flash
# datetime: Para trabalhar com datas e horas.
from datetime import datetime
# Importa as instâncias das extensões inicializadas em 'extensions.py'.
from extensions import bootstrap, moment, db
# Importa os modelos de dados (tabelas do banco) e o formulário.
from models import User, Role, NameForm
# Importa a função factory 'create_app' para criar a instância da aplicação.
from factory import create_app

# Cria a instância da aplicação Flask utilizando a função factory.
# Este padrão ajuda a organizar a aplicação e a evitar importações circulares.
app = create_app()

# Define a rota principal da aplicação ('/').
# O decorator @app.route associa a URL à função 'index'.
# methods=['GET', 'POST'] permite que esta rota aceite tanto requisições GET (para exibir a página)
# quanto POST (geralmente para enviar dados de um formulário).
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    View principal que renderiza a página inicial.
    Processa um formulário para adicionar ou verificar um nome de usuário.
    """
    # Cria uma instância do formulário 'NameForm' que será renderizado no template.
    form = NameForm()
    
    # O método validate_on_submit() retorna True se o formulário foi submetido (requisição POST)
    # e se todos os validadores definidos no formulário passaram.
    if form.validate_on_submit():
        # Busca no banco de dados por um usuário com o nome enviado no formulário.
        # .query.filter_by() cria uma consulta. .first() retorna o primeiro resultado ou None se não encontrar.
        user = User.query.filter_by(username=form.name.data).first()
        
        # Verifica se o usuário não foi encontrado no banco de dados.
        if user is None:
            # Se o usuário é novo, exibe uma mensagem de boas-vindas.
            flash('Novo nome cadastrado!')
            # Cria uma nova instância do modelo 'User' com o nome do formulário.
            user = User(username=form.name.data)
            # Adiciona o novo objeto de usuário à sessão do banco de dados.
            db.session.add(user)
            # Confirma a transação, salvando o novo usuário no banco de dados.
            db.session.commit()
            # Armazena na sessão que este é um usuário novo (não conhecido).
            session['known'] = False
        else:
            # Se o usuário já existe, exibe uma mensagem diferente.
            flash('Nome existente!')
            # Armazena na sessão que este é um usuário já conhecido.
            session['known'] = True
            
        # Armazena o nome enviado no formulário na sessão do usuário.
        # Isso permite que o nome seja lembrado em futuras requisições.
        session['name'] = form.name.data
        # Limpa o campo do formulário após o envio.
        form.name.data = ''
        
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