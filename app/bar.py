from models import Bar as models_bar
from app import db

class Bar:
	def __len__(self):
		return len(models_bar.query.filter().all())

	def last(self):
		return models_bar.query.filter().order_by(models_bar.id.desc()).first()

	def cadastra_bar(self, nome, descricao, endereco, telefone, especialidade, foto):
		new = models_bar(nome.upper(), descricao, endereco, telefone, especialidade, foto)
		db.session.add(new)
		db.session.commit()

	def consulta_bar_todos(self):
		return models_bar.query.filter().all()

	def consulta_bar_por_id(self, id):
		return models_bar.query.filter_by(id=id).first()

	def consulta_bar_por_nome(self, filtro):
		return models_bar.query.filter(models_bar.nome.contains(filtro.upper()))

	def alterar_bar_por_id(self, obj):
		if obj:
			edit = self.consulta_bar_por_id(obj.id)
			if edit:
				edit.nome = obj.nome.upper()
				edit.descricao = obj.descricao
				edit.endereco = obj.endereco
				edit.telefone = obj.telefone
				edit.especialidade = obj.especialidade
				edit.foto = obj.foto
				db.session.commit()
				return edit
		return None

	def remover_bar_por_id(self, id):
		rem = self.consulta_bar_por_id(id)
		if rem:
			db.session.delete(rem)
			db.session.commit()
		return rem