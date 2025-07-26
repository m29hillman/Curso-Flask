# Importa a classe Flask e as funções redirect e abort do pacote flask.
# Flask é a classe principal para criar a aplicação.
# redirect é usada para enviar o cliente (navegador) para outra URL.
# abort é usada para interromper uma requisição com um código de erro HTTP
# (por exemplo, 404 para "Não Encontrado").
from flask import Flask, redirect, abort

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
    # A função redirect() cria uma resposta que instrui o navegador a ir
    # para a URL fornecida. Neste caso, qualquer pessoa que acesse a rota
    # raiz ('/') será imediatamente redirecionada para o Google.
    # O código de status padrão para o redirecionamento é 302 (Found).
    return redirect('https://google.com.br') # Redireciona para o Google

# Associa a URL '/user/<id>' à função get_user.
# O <id> na URL é um parâmetro dinâmico.
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    # Se a função load_user retornar None (ou seja, o usuário não foi encontrado),
    # a função abort(404) é chamada.
    # Ela interrompe a execução da view imediatamente e faz o Flask retornar
    # uma página de erro com o código HTTP 404 (Not Found).
    if not user:
        abort(404)
    return f'<h1>Hello, {user}!</h1>'

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