from models import Bar as _Bar
from app import db

class Bar:
	def __len__(self):
		return len(_Bar.query.filter().all())

	def last(self):
		return _Bar.query.filter().order_by(_Bar.id.desc()).first()

	def cadastra_bar(self, nome, descricao, endereco, telefone, especialidade, foto):
		new = _Bar(nome.upper(), descricao, endereco, telefone, especialidade, foto)
		db.session.add(new)
		db.session.commit()

	def consulta_bar_todos(self):
		return _Bar.query.filter().all()

	def consulta_bar_por_id(self, id):
		return _Bar.query.filter_by(id=id).first()

	def consulta_bar_por_nome(self, filtro):
		return _Bar.query.filter(_Bar.nome.contains(filtro.upper()))

	def alterar_bar(self, obj):
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
		import pdb; pdb.set_trace()
		rem = self.consulta_bar_por_id(id)
		if rem:
			db.session.delete(rem)
			db.session.commit()
		return rem