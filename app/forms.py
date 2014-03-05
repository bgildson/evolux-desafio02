from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class CadastroBarForm(Form):
	nome = TextField('nome', validators=[Required()])
	descricao = TextField('descricao', validators=[Required()])
	endereco = TextField('endereco', validators=[Required()])
	telefone = TextField('telefone', validators=[Required()])
	especialidade = TextField('especialidade', validators=[Required()])
	# falta o campo que ira armazenar a imagem