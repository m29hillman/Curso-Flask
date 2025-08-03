# models/role.py
# Importa a instância do SQLAlchemy (db) do módulo 'extensions'.
# Isso evita importações circulares e segue o padrão de inicialização de extensões.
from extensions import db

# Define o modelo de dados 'Role' que mapeia para a tabela 'roles' no banco de dados.
# A classe Role herda de db.Model, a classe base para todos os modelos do Flask-SQLAlchemy.
class Role(db.Model):
    # __tablename__ especifica o nome da tabela no banco de dados.
    __tablename__ = 'roles'
    
    # Define a coluna 'id' como a chave primária da tabela.
    # db.Column é usado para definir uma coluna.
    # db.Integer especifica o tipo de dado como um inteiro.
    # primary_key=True marca esta coluna como a chave primária.
    id = db.Column(db.Integer, primary_key=True)
    
    # Define a coluna 'name' para armazenar o nome da função/papel (ex: 'Admin', 'User').
    # db.String(64) define o tipo como uma string com um comprimento máximo de 64 caracteres.
    # unique=True garante que cada nome de função na tabela seja único.
    name = db.Column(db.String(64), unique=True)
    
    # Define a relação entre Role e User. Isso não cria uma coluna no banco de dados.
    # 'User' é o nome da classe do modelo do outro lado da relação.
    # backref='role' cria um atributo 'role' nos objetos User, permitindo o acesso
    # reverso (de um usuário para sua função, ex: user.role).
    # lazy='dynamic' faz com que a consulta para os usuários não seja executada
    # imediatamente. Em vez disso, retorna um objeto de consulta que pode ser
    # refinado antes da execução (ex: role.users.order_by(...).all()).
    # Isso é útil para coleções que podem ser muito grandes.
    users = db.relationship('User', backref='role', lazy='dynamic')

    # O método __repr__ (representação) fornece uma representação em string "oficial" do objeto.
    # É útil para depuração, pois permite ver uma representação legível do objeto
    # ao imprimi-lo ou exibi-lo no console.
    def __repr__(self):
        return f'<Role {self.name}>'