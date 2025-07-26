# Importa a classe Flask para criar a aplicação, e as funções `render_template` para renderizar templates HTML,
# `session` para gerenciar sessões de usuário, `redirect` e `url_for` para redirecionamentos, e `flash` para exibir mensagens temporárias.
from flask import Flask, render_template, session, redirect, url_for, flash
# Importa a extensão Flask-Bootstrap para integrar o framework Bootstrap.
from flask_bootstrap import Bootstrap
# Importa a classe principal da extensão Flask-Moment, que integra a biblioteca moment.js.
from flask_moment import Moment
# Importa a classe principal da extensão Flask-WTF, que integra a biblioteca wtforms.
from flask_wtf import FlaskForm
# Importa os tipos de campo `StringField` (para texto) e `SubmitField` (para botão de envio) do WTForms.
from wtforms import StringField, SubmitField
# Importa o validador `DataRequired`, que garante que um campo não seja enviado vazio.
from wtforms.validators import DataRequired
# Importa a classe datetime do módulo padrão do Python para trabalhar com datas e horas.
from datetime import datetime

# Define uma classe de formulário `NameForm` que herda de `FlaskForm`.
class NameForm(FlaskForm):
    # Cria um campo de texto com o rótulo 'Qual é o seu nome?' e um validador que exige preenchimento.
    name = StringField('Qual é o seu nome?', validators=[DataRequired()])
    # Cria um botão de envio com o rótulo 'Enviar'.
    submit = SubmitField('Enviar')

# Cria a instância principal da aplicação Flask.
app = Flask(__name__)
# Configura uma chave secreta para a aplicação, usada para proteger sessões e outros dados de segurança.
# É uma boa prática armazenar isso em uma variável de ambiente.
app.config['SECRET_KEY'] = 'chave secreta que deve ser bem complexa'

# Inicializa o Flask-Bootstrap na nossa aplicação.
bootstrap = Bootstrap(app)
# Inicializa o Flask-Moment na nossa aplicação.
moment = Moment(app)

# Define uma rota para a URL '/'
# Aceita tanto requisições GET (para exibir a página) quanto POST (para enviar o formulário).
@app.route('/', methods=['GET', 'POST'])
def index():
    # Cria uma instância do formulário `NameForm`.
    form = NameForm()
    # Verifica se o formulário foi submetido e se todos os dados são válidos.
    if form.validate_on_submit():
        # Obtém o nome anteriormente armazenado na sessão, se houver.
        old_name = session.get('name')
        # Verifica se já existia um nome na sessão e se o novo nome é diferente.
        if old_name is not None and old_name != form.name.data:
            # Se o nome foi alterado, exibe uma mensagem para o usuário no próximo request.
            flash('Você alterou seu nome!')
        # Armazena o novo nome enviado pelo formulário na sessão do usuário.
        session['name'] = form.name.data
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