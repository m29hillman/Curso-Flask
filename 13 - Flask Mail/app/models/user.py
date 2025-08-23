# models/user.py
# Importa a instância do SQLAlchemy (db) do módulo 'extensions'.
# Isso evita importações circulares e segue o padrão de inicialização de extensões.
from extensions import db

# Define o modelo de dados 'User' que mapeia para a tabela 'users' no banco de dados.
# A classe User herda de db.Model, a classe base para todos os modelos do Flask-SQLAlchemy.
class User(db.Model):
    # __tablename__ especifica o nome da tabela no banco de dados.
    __tablename__ = 'users'
    
    # Define a coluna 'id' como a chave primária da tabela.
    # db.Column é usado para definir uma coluna.
    # db.Integer especifica o tipo de dado como um inteiro.
    # primary_key=True marca esta coluna como a chave primária.
    id = db.Column(db.Integer, primary_key=True)
    
    # Define a coluna 'username' para armazenar o nome do usuário.
    # db.String(80) define o tipo como uma string com um comprimento máximo de 80 caracteres.
    # unique=True garante que cada nome de usuário na tabela seja único.
    # nullable=False significa que esta coluna não pode ter valores nulos (deve ser preenchida).
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # Define a coluna 'role_id' como uma chave estrangeira.
    # db.ForeignKey('roles.id') cria uma restrição de chave estrangeira,
    # ligando esta coluna à coluna 'id' da tabela 'roles'.
    # Isso estabelece a relação "um-para-muitos" entre Role e User (uma Role pode ter muitos Users).
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # O método __repr__ (representação) fornece uma representação em string "oficial" do objeto.
    # É útil para depuração, pois permite ver uma representação legível do objeto
    # ao imprimi-lo ou exibi-lo no console.
    def __repr__(self):
        return f'<User {self.username}>'