from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class CadastroBarForm(Form):
	req = Required('Campo Requerido') # generaliza msgs de campo requerido
	nome = TextField('nome', validators=[req])
	descricao = TextField('descricao', validators=[req])
	endereco = TextField('endereco', validators=[req])
	telefone = TextField('telefone', validators=[req])
	especialidade = TextField('especialidade', validators=[req])
	# falta o campo que ira armazenar a imagem