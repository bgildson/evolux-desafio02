from app import db

class Bar(db.Model):
	__tablename__ = 'cad_bares'
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(60))
	descricao = db.Column(db.String(100))
	endereco = db.Column(db.String(90))
	telefone = db.Column(db.String(50))
	especialidade = db.Column(db.String(60))
	foto = db.Column(db.String(30))

	def __init__(self, nome, descricao, endereco, telefone, especialidade, foto, id=0):
		self.nome = nome
		self.descricao = descricao
		self.endereco = endereco
		self.telefone = telefone
		self.especialidade = especialidade
		self.foto = foto
		if id > 0:
			self.id = id