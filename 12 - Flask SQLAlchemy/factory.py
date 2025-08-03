# Importações de pacotes e módulos necessários.
# Flask: Classe principal para criar a aplicação.
from flask import Flask
# Importa as instâncias das extensões criadas em 'extensions.py'.
from extensions import db, bootstrap, moment
# os: Módulo para interagir com o sistema operacional, usado aqui para construir caminhos de arquivo.
import os

# Define o caminho absoluto para o diretório onde este arquivo (factory.py) está localizado.
# Isso garante que o caminho para o banco de dados SQLite seja sempre correto,
# independentemente de onde o script é executado.
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    """
    Função Factory para criar e configurar a instância da aplicação Flask.
    Este padrão permite criar múltiplas instâncias da aplicação com diferentes configurações,
    o que é útil para testes e evita problemas de importação circular.
    """
    # Cria a instância principal da aplicação Flask.
    # __name__ é o nome do módulo Python atual. Flask usa isso para localizar recursos.
    app = Flask(__name__)
    
    # --- Configurações da Aplicação ---
    # Chave secreta usada para segurança, como assinar cookies de sessão.
    # IMPORTANTE: Em produção, esta chave deve ser longa, aleatória e mantida em segredo,
    # geralmente carregada de uma variável de ambiente.
    app.config['SECRET_KEY'] = 'chave secreta que deve ser bem complexa'
    
    # Configura o URI do banco de dados para o Flask-SQLAlchemy.
    # Aqui, estamos usando um banco de dados SQLite chamado 'data.sqlite'
    # localizado no mesmo diretório da aplicação.
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        
    # Desativa o recurso de rastreamento de modificações do SQLAlchemy,
    # que não é necessário e consome recursos extras.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # --- Inicialização das Extensões ---
    # Associa as instâncias das extensões (db, bootstrap, moment) com a aplicação 'app'.
    # O método .init_app() permite que as extensões sejam inicializadas separadamente
    # da criação da aplicação, o que é essencial para o padrão factory.
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    # --- Criação do Banco de Dados ---
    # O 'app_context' garante que a aplicação esteja configurada corretamente
    # antes de interagir com suas extensões, como o banco de dados.
    with app.app_context():
        # db.create_all() cria todas as tabelas definidas nos modelos (em models.py)
        # que ainda não existem no banco de dados.
        # Em um ambiente de produção, é mais comum usar ferramentas de migração
        # como o Flask-Migrate para gerenciar as alterações no esquema do banco de dados.
        db.create_all()

    # Retorna a instância da aplicação configurada.
    return app