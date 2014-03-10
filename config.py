import os
from os.path import realpath

# formularios
CSRF_ENABLED = True
SECRET_KEY = 'evolux-desafio-csrf-key'

basedir = os.path.abspath(os.path.dirname(__file__))

# banco de dados
SQLALCHEMY_DATABASE_NAME = 'app'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/app.db')

UPLOAD_FROM_PATH = os.path.join('app', 'static', 'upload')
UPLOAD_FROM_TEMPLATES = os.path.join('..', 'static', 'upload')
FOTO_PADRAO = '0.jpg'