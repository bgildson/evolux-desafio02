#from app import app
import sqlite3
from os.path import realpath

class Bar:
	__slots__ = 'id', 'nome', 'descricao', 'endereco', 'telefone', 'especialidade', 'foto'
	# preeche o objeto a partir de um objeto de consulta do cursor
	def __init__(self):
		self.id = 0
		self.nome = ''
		self.descricao = ''
		self.endereco = ''
		self.telefone = ''
		self.especialidade = ''
		self.foto = None

	# python nao tem SOBRECARGA DE METODOS... tive que fazer dois metodos que seriam os construtores do objeto
	def preenche_de_obj_consulta(self, obj):
		self.id = obj['id']
		self.nome = obj['nome']
		self.descricao = obj['descricao']
		self.endereco = obj['endereco']
		self.telefone = obj['telefone']
		self.especialidade = obj['especialidade']
		self.foto = obj['foto']

	def preenche_de_campos(self, id, nome, descricao, endereco, telefone, especialidade, foto):
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
		self.__connection = sqlite3.connect(realpath('app/app.py'))
		self.__connection.row_factory = sqlite3.Row # faz com que o acesso as colunas seja direto pelo nome, Ex.: cursor['nome_coluna']
		self.__cur = self.__connection.cursor()
		print (self.__cur)

	def close(self):
		self.__connection.commit()
		self.__connection = None
		self.__cur = None

	def cadastra_bar(self, nome, descricao, endereco, telefone, especialidade, foto = 0):
		self.__cur.execute('INSERT INTO cad_bares (nome, descricao,endereco, telefone, especialidade, foto) VALUES (?, ?, ?, ?, ?, ?)', (nome, descricao, endereco, telefone, especialidade, foto))

	def consulta_bar_geral(self, filtro):
		self.open()
		results = self.__cur.execute('SELECT * FROM cad_bares WHERE nome LIKE \'%?%\' OR descricao LIKE \'%?%\' OR endereco LIKE \'%?%\' OR telefone LIKE \'%?%\' OR especialidade LIKE \'%?%\'', (filtro, filtro, filtro, filtro, filtro))
		#results = self.__cur.execute('SELECT * FROM cad_bares WHERE nome LIKE \'%' + str(filtro) + '%\' OR descricao LIKE \'%' + str(filtro) + '%\' OR endereco LIKE \'%' + str(filtro) + '%\' OR telefone LIKE \'%' + str(filtro) + '%\' OR especialidade LIKE \'%' + str(filtro) + '%\'')
		self.close()
		#sql = 'SELECT * FROM cad_bares WHERE nome LIKE \'%' + str(filtro) + '%\' OR descricao LIKE \'%' + str(filtro) + '%\' OR endereco LIKE \'%' + str(filtro) + '%\' OR telefone LIKE \'%' + str(filtro) + '%\' OR especialidade LIKE \'%' + str(filtro) + '%\''
		#results = self.__cur.execute(sql)
		return self.__consulta_p_objeto(results)

	def consulta_bar_por_id(self, id):
		results = self.__cur.execute('SELECT * FROM cad_bares WHERE id = ?', (id))
		#results = self.__cur.execute(sql).fetchall()
		return self.__consulta_p_objeto(results)

	def alterar_bar(self, id, nome, descricao, endereco, telefone, especialidade, foto):
		r = consulta_bar_por_id(id)
		self.__cur.execute('UPDATE cad_bares SET nome = \'?\', descricao = \'?\', endereco = \'?\', telefone = \'?\', especialidade = \'?\', foto = ? WHERE id = ?', (nome, descricao, endereco, telefone, especialidade, foto))
		#sql = 'UPDATE cad_bares SET nome = \'' + nome + '\', descricao = \'' + descricao + '\', endereco = \'' + endereco + '\', telefone = \'' + telefone + '\', especialidade = \'' + especialidade + '\', foto = ' + str(foto) + ' WHERE id = ' + str(id)
		#self.__cur.execute(sql)
		return r

	def remove_bar(self, id):
		r = consulta_bar_por_id(id)
		self.__cur.execute('DELETE FROM cad_bares WHERE id = ?', (id))
		#sql = 'DELETE FROM cad_bares WHERE id = ' + str(id)
		#self.__cur.execute(sql)
		return r

	def __consulta_p_objeto(self, results):
		#print len(results)
		#if (len(results) > 0):
			r = []
			for result in results:
				b = Bar()
				b.preenche_de_obj_consulta(result)
				r.append(b)
			return r
		#return None

#dao = DaoDB()
#dao.open()
#obj = dao.consulta_bar_geral('il')
#dao.cadastra_bar(u'genilson', u'qlqr uma', u'sem endereco', u'sem telefone', u'sem especialidade', u'0')
#dao.close()
#for o in obj:
#	print (o.nome)
#	print (o.descricao)
#	print (o.telefone)
#	print(isinstance(o,Bar))