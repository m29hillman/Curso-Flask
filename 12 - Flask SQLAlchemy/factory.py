# Importa a classe Flask para criar a aplicação, e as funções `render_template` para renderizar templates HTML,
# `session` para gerenciar sessões de usuário, `redirect` e `url_for` para redirecionamentos, e `flash` para exibir mensagens temporárias.
from flask import Flask
from extensions import db, bootstrap, moment
import os

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    # Cria a instância principal da aplicação Flask.
    app = Flask(__name__)
    # Configura uma chave secreta para a aplicação, usada para proteger sessões e outros dados de segurança.
    # É uma boa prática armazenar isso em uma variável de ambiente.
    app.config['SECRET_KEY'] = 'chave secreta que deve ser bem complexa'
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializa as extensões
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    with app.app_context():
        db.create_all()

    return app