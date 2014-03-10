# -*- coding: cp1252 -*-
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from flask.ext.uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)
req = Required('Campo Necessário'.decode('utf-8')) # generaliza msgs de campo requerido

class CadastroBarForm(Form):
	id = TextField('id')
	nome = TextField('nome', validators=[req])
	descricao = TextField('descricao', validators=[req])
	endereco = TextField('endereco', validators=[req])
	telefone = TextField('telefone', validators=[req])
	especialidade = TextField('especialidade', validators=[req])
	foto = FileField('foto', validators=[FileAllowed(['jpg', 'png'], 'Somente imagens! (JPG, PNG)')])

class ConsultaForm(Form):
	consulta = TextField('consulta', validators=[req])