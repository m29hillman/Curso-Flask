from flask import Flask, render_template, session, redirect, url_for, flash
from datetime import datetime
from extensions import bootstrap, moment, db
from models import User, Role, NameForm
from factory import create_app

app = create_app()

# Define uma rota para a URL '/'
# Aceita tanto requisições GET (para exibir a página) quanto POST (para enviar o formulário).
@app.route('/', methods=['GET', 'POST'])
def index():
    # Cria uma instância do formulário `NameForm`.
    form = NameForm()
    # Verifica se o formulário foi submetido e se todos os dados são válidos.
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            flash('Novo nome cadastrado!')
            # Se o usuário não existir, cria um novo usuário com o nome fornecido.
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            flash('Nome existente!')
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        # Redireciona o usuário para a mesma página (padrão Post/Redirect/Get) para evitar reenvio do formulário ao recarregar a página.
        return redirect(url_for('index'))
    # Renderiza o template `index.html`, passando o formulário, o nome da sessão e a hora atual para serem exibidos.
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())

# Define um manipulador de erro para o código de status 404 (Página não encontrada).
@app.errorhandler(404)
def page_not_found(e):
    # Renderiza um template específico para a página de erro 404.
    return render_template('404.html'), 404


# Quando um erro 500 ocorre em qualquer parte da aplicação
@app.errorhandler(500)
def internal_server_error(e):
    # Renderiza um template específico para a página de erro 500.
    return render_template('500.html'), 500

# Bloco de execução principal: só roda quando o script é executado diretamente.
if __name__ == "__main__":
    # Inicia o servidor de desenvolvimento integrado do Flask.
    # ATENÇÃO: Nunca use o servidor de desenvolvimento em produção.
    app.run(
        host='0.0.0.0',  # Acessível de qualquer IP na rede.
        port=5000,       # Porta padrão do Flask.
        debug=True,      # Ativa o modo de depuração (recarregamento automático e debugger).
        threaded=True    # Permite processar múltiplas requisições simultaneamente.
    )