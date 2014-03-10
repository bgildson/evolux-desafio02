# -*- coding: cp1252 -*-
from flask import render_template, redirect, request, url_for, flash
from werkzeug.utils import secure_filename
import os
from app import app
from forms import CadastroBarForm, ConsultaForm
from bar import Bar as BarOperacoes

bar = BarOperacoes()

def get_extension(name):
	return name.split('.')[-1]

# salva ou seleciona uma foto de acordo com os parametros passados
def salvar_foto(foto=None, id=None):
	filename = ''
	if foto:
		filename = secure_filename(foto.filename)
		if id:
			filename = '%s.%s' % (id, get_extension(filename))
		else:
			last = bar.last()
			if last:
				filename = '%s.%s' % (str(int(last.id) + 1), get_extension(filename))
			else:
				filename = '1.%s' % get_extension(filename)
		foto.save(os.path.join(app.config['UPLOAD_FROM_PATH'], filename))
		foto.close()
	else:
		filename = app.config['FOTO_PADRAO']
	return filename

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	form = CadastroBarForm()
	import pdb; pdb.set_trace()
	if form.validate_on_submit() and request.method == 'POST':
		filename = salvar_foto(foto=form.foto.data)
		bar.cadastra_bar(form.nome.data, form.descricao.data, form.endereco.data, form.telefone.data, form.especialidade.data, filename)
		flash('Bar, %s, cadastrado com sucesso!' % form.nome.data)
		form = CadastroBarForm()
		return render_template('cadastro.html', title='Cadastro', form=form, foto=os.path.join(app.config['UPLOAD_FROM_TEMPLATES'], filename))
	return render_template('cadastro.html', title='Cadastro', form=form)

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
	form = ConsultaForm()
	if request.method == 'POST' and form.validate_on_submit():
		filtro = form.consulta.data
		resultados = bar.consulta_bar_por_nome(filtro) 

		return render_template('consulta.html', title='Consulta', form=form, resultados=resultados, filtro=filtro, caminho_foto=app.config['UPLOAD_FROM_TEMPLATES'])
	return render_template('consulta.html', title='Consulta', form=form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
	form = CadastroBarForm()
	result = bar.consulta_bar_por_id(id)
	if result:
		form.id.data = result.id
		form.nome.data = result.nome
		form.descricao.data = result.descricao
		form.endereco.data = result.endereco
		form.telefone.data = result.telefone
		form.especialidade.data = result.especialidade
		return render_template('editar.html', title='Editar', form=form, foto=os.path.join(app.config['UPLOAD_FROM_TEMPLATES'], result.foto))
	return redirect( url_for('home'), message='Usuário com ID %s não encontrado.' % id)

@app.route('/salvar_edicao/<id>', methods=['GET', 'POST'])
def salvar_edicao(id):
	form = CadastroBarForm()
	result = bar.consulta_bar_por_id(id)
	if form.validate_on_submit() and result:
		form.id.data = result.id
		result.id
		result.nome = form.nome.data
		result.descricao = form.descricao.data
		result.endereco = form.endereco.data
		result.telefone = form.telefone.data
		result.especialidade = form.especialidade.data
		foto_old = result.foto
		if form.foto.data:
			result.foto = salvar_foto(foto=form.foto.data, id=result.id)
			if foto_old != result.foto:
				# remove a foto, pois nao sera mais utilizada
				os.remove(os.path.join(app.config['UPLOAD_FROM_PATH'], foto_old))
		bar.alterar_bar(result)
	return redirect(url_for('editar', id=id))
	
@app.route('/remover/<int:id>', methods=['GET', 'POST'])
def remover(id=None):
	form = CadastroBarForm()
	if id:
		rem = bar.remover_bar_por_id(id)
		if rem:
			# remove a foto, pois nao sera mais utilizada
			os.remove(os.path.join(app.config['UPLOAD_FROM_PATH'], rem.foto))
			return render_template('index.html', title='Home', message=rem.nome)
		return render_template('editar.html', title='Editar', id=id)
	return render_template('editar.html', title='Editar', form=form)