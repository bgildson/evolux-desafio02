from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from flask.ext.uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)
req = Required('Campo Requerido') # generaliza msgs de campo requerido

class CadastroBarForm(Form):
	nome = TextField('nome', validators=[req])
	descricao = TextField('descricao', validators=[req])
	endereco = TextField('endereco', validators=[req])
	telefone = TextField('telefone', validators=[req])
	especialidade = TextField('especialidade', validators=[req])
	upload = FileField('image', validators=[FileAllowed(images, 'Somente imagens!')])

class ConsultaForm(Form):
	consulta = TextField('consulta', validators=[Required(req)])