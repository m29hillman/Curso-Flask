# Importa a classe Flask e as funções render_template e abort do pacote flask.
from flask import Flask, render_template, abort
# Importa a extensão Flask-Bootstrap para integrar o framework Bootstrap.
from flask_bootstrap import Bootstrap

# Função de exemplo para simular a busca de um usuário no banco de dados.
# Em uma aplicação real, aqui ocorreria uma consulta a um banco de dados.
def load_user(id):
    # O ID '6900' é usado para simular um usuário encontrado.
    if id == '6900':
        # Retornar um dicionário é mais realista, simulando um objeto de usuário.
        return {'name': 'Marcelo Mazzochi Hillman', 'id': id}
    else:
        # Retorna None se o usuário não for encontrado.
        return None

# Cria a instância principal da aplicação Flask.
# __name__ é usado pelo Flask para localizar recursos (templates, arquivos estáticos).
app = Flask(__name__)

# Inicializa o Flask-Bootstrap na nossa aplicação.
# Isso permite que nossos templates herdem de um template base do Bootstrap,
# facilitando o uso de seus componentes de CSS e JavaScript sem configuração manual.
bootstrap = Bootstrap(app)

# Define uma rota para a URL '/user/<id>', onde <id> é um parâmetro dinâmico.
@app.route('/user/<id>')
def get_user(id):
    """Busca um usuário pelo ID e renderiza a página de perfil."""
    user = load_user(id)
    if not user:
        # Se o usuário não for encontrado, a função abort() é chamada para
        # interromper a requisição e retornar um código de erro HTTP, neste caso 404.
        abort(404)
    # Renderiza o template 'user.html', passando o objeto do usuário.
    # As informações do usuário (como 'name') estarão disponíveis no template.
    return render_template('user.html', name=user['name'])

# Define um manipulador de erro personalizado para o código 404 (Not Found).
# Quando um erro 404 ocorre em qualquer parte da aplicação (seja por uma URL
# inválida ou por um abort(404)), esta função é executada.
@app.errorhandler(404)
def page_not_found(e):
    # Renderiza um template específico para a página de erro 404.
    # O 'e' contém informações sobre o erro.
    # Retornamos o template e o código de status 404.
    return render_template('404.html'), 404

# Define um manipulador de erro personalizado para o código 500 (Internal Server Error).
# Quando um erro 500 ocorre em qualquer parte da aplicação (seja por uma URL
# inválida ou por um abort(500)), esta função é executada.
@app.errorhandler(500) 
def internal_server_error(e):
    # Renderiza um template específico para a página de erro 500.
    # O 'e' contém informações sobre o erro.
    # Retornamos o template e o código de status 500.
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