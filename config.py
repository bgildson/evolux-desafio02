# formularios
CSRF_ENABLED = True
SECRET_KEY = 'evolux-desafio-csrf-key'

# banco de dados
SQLALCHEMY_DATABASE_NAME = 'app'
SQLALCHEMY_DATABASE_URI = 'sqlite:///app/' + SQLALCHEMY_DATABASE_NAME + '.db'