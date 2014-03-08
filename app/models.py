from app import db

class Bar(db.Model):
	__tablename__ = 'cad_bares'
	id = db.Column(db.Integer, primary_key = True, nullable=False)
	nome = db.Column(db.String(60), nullable=False)
	descricao = db.Column(db.String(100), nullable=False)
	endereco = db.Column(db.String(90), nullable=False)
	telefone = db.Column(db.String(50), nullable=False)
	especialidade = db.Column(db.String(60), nullable=False)
	foto = db.Column(db.String(30), nullable=False)

	def __init__(self, nome, descricao, endereco, telefone, especialidade, foto, id=0):
		self.nome = nome
		self.descricao = descricao
		self.endereco = endereco
		self.telefone = telefone
		self.especialidade = especialidade
		self.foto = foto
		if id > 0:
			self.id = id