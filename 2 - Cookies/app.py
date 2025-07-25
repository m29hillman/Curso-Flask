# Importa a classe Flask e a função make_response do pacote flask.
# Flask é a classe principal para criar a aplicação.
# make_response é uma função auxiliar para criar um objeto de resposta completo,
# permitindo a manipulação de cabeçalhos (headers) e cookies.
# request é um objeto que contém as informações da requisição HTTP enviada pelo cliente.
from flask import Flask, make_response, request

# Cria uma instância da classe Flask.
# O argumento `__name__` é uma variável especial do Python que contém o nome
# do módulo atual. O Flask a utiliza para localizar recursos como templates
# e arquivos estáticos.
app = Flask(__name__)

# Associa a URL raiz ('/') à função index.
@app.route('/')
def index():
    """
    Esta view demonstra a criação de um objeto de resposta e a definição de um cookie.
    """
    # A função make_response() cria um objeto de resposta (Response object).
    # Ter um objeto de resposta nos permite manipular vários aspectos da resposta HTTP
    # antes de enviá-la ao cliente.
    #
    # Propriedades e métodos comuns do objeto de resposta:
    # - response.headers: Um dicionário para adicionar/modificar cabeçalhos HTTP.
    #   Ex: response.headers['X-Custom-Header'] = 'My Value'
    # - response.status_code: Define o código de status HTTP (ex: 200, 404, 500).
    # - response.mimetype: Define o tipo de conteúdo (header Content-Type).
    #   Ex: response.mimetype = 'application/json'
    # - response.set_cookie(): Define um cookie no navegador do cliente.
    # - response.delete_cookie(): Remove um cookie do navegador do cliente.
    #
    response = make_response('<h1>Este documento define um cookie! Visite /read-cookie para vê-lo.</h1>')

    # Usa o método `set_cookie()` do objeto de resposta para adicionar um cookie.
    # O primeiro argumento é o nome do cookie ('username') e o segundo é o seu valor ('Marcelo').
    # Este cookie será armazenado no navegador do usuário.
    response.set_cookie('username', 'Marcelo')

    # Retorna o objeto de resposta modificado. O Flask o enviará para o navegador.
    return response

# Esta rota lê e exibe o valor de um cookie que foi previamente definido.
@app.route('/read-cookie')
def read_cookie():
    """Lê e exibe o valor de um cookie armazenado no navegador."""
    # O objeto `request` contém todas as informações da requisição HTTP recebida.
    # `request.cookies` é um dicionário que armazena todos os cookies enviados pelo cliente.
    # Usamos o método .get() para acessar o cookie 'username' de forma segura,
    # retornando 'visitante' como valor padrão se o cookie não for encontrado.
    username = request.cookies.get('username', 'visitante')
    return f'<h1>Bem-vindo de volta, {username}!</h1>'

# Esta rota demonstra como remover um cookie do navegador.
@app.route('/delete-cookie')
def delete_cookie():
    """Cria uma resposta que instrui o navegador a deletar um cookie."""
    # Criamos uma resposta para o cliente.
    response = make_response('<h1>Cookie removido! Visite /read-cookie para confirmar.</h1>')

    # O método `delete_cookie()` define um cookie com o mesmo nome,
    # mas com uma data de expiração no passado, o que faz com que o navegador o remova.
    response.delete_cookie('username')

    return response

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