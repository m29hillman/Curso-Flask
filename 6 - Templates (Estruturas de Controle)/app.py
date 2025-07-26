# Importa a classe Flask e as funções render_template, redirect e abort do pacote flask.
# Flask é a classe principal para criar a aplicação.
# render_template é usada para renderizar um template HTML, permitindo passar variáveis do Python para o template.
from flask import Flask, render_template

# Esta é uma função de exemplo para simular a busca de um usuário.
# Em uma aplicação real, esta função provavelmente faria uma consulta
# a um banco de dados (como SQL ou NoSQL) para encontrar o usuário
# com o ID fornecido. Aqui, apenas verificamos um valor fixo para
# demonstrar a lógica de encontrar ou não um usuário e como a view
# reage a isso.
def load_user(id):
    if(id=='6900'):
        return 'Marcelo Mazzochi Hillman'
    else:
        return None

# Cria uma instância da classe Flask.
# O argumento `__name__` é uma variável especial do Python que contém o nome
# do módulo atual. O Flask a utiliza para localizar recursos como templates
# e arquivos estáticos.
app = Flask(__name__)

# Associa a URL raiz ('/') à função index.
@app.route('/')
def index():
    # A função render_template busca por um arquivo chamado 'index.html' na pasta 'templates'
    # (por padrão) e o renderiza. O resultado é uma string HTML que é enviada como
    # resposta para o navegador do cliente.
    return render_template('index.html')

# Associa a URL '/user/<id>' à função get_user.
# O <id> na URL é um parâmetro dinâmico.
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    # Aqui, render_template não apenas renderiza o template 'user.html', mas também
    # passa uma variável para ele. O argumento `name=user` torna a variável `name`
    # disponível dentro do template 'user.html', com o valor da variável `user` do Python.
    # No template, você pode usar {{ name }} para exibir o nome do usuário.
    return render_template('user.html', name=user)

# Associa a URL '/users' à função get_users.
@app.route('/users')
def get_users():
    users = ['Marcelo', 'Joao', 'Pedro', 'Maria']
    # Aqui, render_template renderiza o template 'users.html' e passa a lista de usuários para ele.
    # O argumento `usuarios=users` torna a variável `usuarios` disponível dentro do template 'users.html',
    # contendo a lista `users` do Python.
    # No template, você pode usar um laço (como for do Jinja2) para iterar sobre a lista `usuarios` e exibir cada nome.
    return render_template('users.html', usuarios=users)

# A condição `if __name__ == "__main__":` garante que o servidor de
# desenvolvimento só seja executado quando este script for executado diretamente
# (e não quando for importado por outro módulo).
if __name__ == "__main__":
    # Inicia o servidor de desenvolvimento integrado do Flask.
    #
    # Parâmetros comuns do `app.run()`:
    # host='0.0.0.0': Faz com que o servidor seja acessível a partir de qualquer
    #                 dispositivo na mesma rede, não apenas do 'localhost' (127.0.0.1).
    #                 Útil para testar a aplicação em celulares ou outros computadores.
    #
    # port=5000:      Define a porta em que o servidor irá escutar por requisições.
    #                 O padrão é 5000.
    #
    # debug=True:     Ativa o modo de depuração. Com ele, o servidor reinicia
    #                 automaticamente a cada alteração no código e exibe um
    #                 depurador interativo no navegador se ocorrer um erro.
    #
    # threaded=True:  Permite que o servidor de desenvolvimento processe múltiplas
    #                 requisições ao mesmo tempo, o que se aproxima mais do
    #                 comportamento de um servidor de produção.
    # **AVISO**: Nunca use o servidor de desenvolvimento em um ambiente de produção.
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)