from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

global app
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import views
import daoDB