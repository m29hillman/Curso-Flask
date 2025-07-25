# Importa a classe Flask do pacote flask. Flask é a classe principal
# que usaremos para criar e gerenciar nossa aplicação web.
from flask import Flask

# Cria uma instância da classe Flask.
# O argumento `__name__` é uma variável especial do Python que contém o nome
# do módulo atual. O Flask a utiliza para localizar recursos como templates
# e arquivos estáticos.
app = Flask(__name__)


# O decorador `@app.route()` é usado para associar uma URL a uma função.
# Quando um navegador solicita a URL raiz ('/'), o Flask invoca a função `index()`
# e envia o valor de retorno dela de volta para o navegador.
@app.route('/')
def index():
    """Esta é a view para a página inicial."""
    return '<h1>Hello World!</h1>'


# Esta rota demonstra como retornar um código de status HTTP diferente.
# Por padrão, o Flask retorna o código 200 (OK).
@app.route('/bad')
def bad_request():
    """Retorna uma resposta de erro 400 - Bad Request."""
    # Ao retornar uma tupla, podemos especificar o corpo da resposta
    # e o código de status. O formato é (corpo, status_code).
    # O navegador receberá o status 400, indicando um erro do cliente.
    return '<h1>Bad Request!</h1>', 400

# Esta é uma rota dinâmica. A parte `<name>` na URL é um placeholder.
# Qualquer texto colocado nessa parte da URL será capturado e passado
# como o argumento `name` para a função `user()`.
@app.route('/user/<name>')
def user(name):
    """Esta view recebe um nome e exibe uma saudação personalizada."""
    # Usamos uma f-string para criar uma resposta HTML dinâmica.
    return f'<h1>Hello, {name}!</h1>'


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
