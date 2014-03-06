from app import app
import sqlite3

class Bar:
	__slots__ = 'id', 'nome', 'descricao', 'endereco', 'telefone', 'especialidade', 'foto'
	# preeche o objeto a partir de um objeto do banco de dados
	def __init__(self, obj):
		self.id = obj['id']
		self.nome = obj['nome']
		self.descricao = obj['descricao']
		self.endereco = obj['endereco']
		self.telefone = obj['telefone']
		self.especialidade = obj['especialidade']
		self.foto = obj['foto']

	def __init__(self, id, nome, descricao, endereco, telefone, especialidade, foto):
		self.id = id
		self.nome = nome
		self.descricao = descricao
		self.endereco = endereco
		self.telefone = telefone
		self.especialidade = especialidade
		self.foto = foto

class DaoDB:
	__slots__ = '__cur', '__connection'
	def __init__(self):
		self.__connection = None
		self.__cur = None
		
	def open(self):
		self.__connection = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_NAME'] + '.db')
		self.__connection.row_factory = sqlite3.Row # faz com que o acesso as colunas seja direto pelo nome, Ex.: cursor['nome_coluna']
		self.__cur = self.__connection.cursor()

	def close(self):
		self.__connection.commit()
		self.__connection = None
		self.__cur = None

	def cadastra_bar(self, nome, descricao, endereco, telefone, especialidade, foto):
		sql = '''INSERT INTO cad_bares (nome, descricao,endereco, telefone, especialidade, foto) 
					VALUES (nome, descricao, endereco, telefone, especialidade, foto)'''
		self.__curr.execute(sql)

	def consulta_bar(self, filtro):
		sql = 'SELECT * FROM cad_bares WHERE nome LIKE \'%' + filtro + '%\' OR descricao LIKE \'%' + filtro + '%\' OR endereco LIKE \'%' + filtro + '%\' OR telefone LIKE \'%' + filtro + '%\' OR especialidade LIKE \'%' + filtro + '%\''
		results = self.__curr.execute(sql).fetchall()
		return self.__consulta_p_objeto(results)

	def consulta_bar_por_id(self, id):
		sql = 'SELECT * FROM cad_bares WHERE id = ' + str(id)
		results = self.__curr.execute(sql).fetchall()
		return self.__consulta_p_objeto(results)

	def alterar_bar(self, id, nome, descricao, endereco, telefone, especialidade, foto):
		r = consulta_bar_por_id(id)
		sql = 'UPDATE cad_bares SET nome = \'' + nome + '\', descricao = \'' + descricao + '\', endereco = \'' + endereco + '\', telefone = \'' + telefone + '\', especialidade = \'' + especialidade + '\', foto = ' + str(foto) + ' WHERE id = ' + str(id)
		self.__curr.execute(sql)
		return r

	def remove_bar(self, id):
		r = consulta_bar_por_id(id)
		sql = 'DELETE FROM cad_bares WHERE id = ' + str(id)
		self.__curr.execute(sql)
		return r

	def __consulta_p_objeto(self, results):
		if (len(results) > 0):
			r = []
			for result in results:
				r.append(Bar(result))
			return r
		return None