"""
Arquivo principal da aplicação Flask.
"""


# Cria a instância da aplicação Flask utilizando a função factory.
# O padrão Factory evita importações circulares e permite múltiplas instâncias/configurações.
#import os 
from app import create_app, db 
from app.models import User, Role 
#from flask_migrate import Migrate

app = create_app('development') 

#migrate = Migrate(app, db)

@app.shell_context_processor 
def make_shell_context(): 
    dict(db=db, User=User, Role=Role)

# Bloco de execução principal: só roda quando o script é executado diretamente.
if __name__ == "__main__":
    # Inicia o servidor de desenvolvimento integrado do Flask.
    # ATENÇÃO: Nunca use o servidor de desenvolvimento em produção.
    app.run(
        host='0.0.0.0',  # Torna o servidor acessível a partir de qualquer IP na rede.
        port=5000,       # Define a porta em que o servidor irá escutar.
        debug=True,      # Ativa o modo de depuração para recarregamento automático e debugger interativo.
        threaded=True    # Permite que o servidor processe múltiplas requisições simultaneamente.
    )