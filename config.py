import os

# formularios
CSRF_ENABLED = True
SECRET_KEY = 'evolux-desafio-csrf-key'

basedir = os.path.abspath(os.path.dirname(__file__))

# banco de dados
SQLALCHEMY_DATABASE_NAME = 'app'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #'sqlite:///' + '.db'