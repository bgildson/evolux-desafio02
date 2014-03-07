from . import db

class cad_bares(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(60))
	descricao = db.Column(db.String(100))
	endereco = db.Column(db.String(90))
	telefone = db.Column(db.String(50))
	especialidade = db.Column(db.String(60))
	foto = db.Column(db.Binary)