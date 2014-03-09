# -*- coding: cp1252 -*-
from flask import Flask, render_template, redirect, request, url_for, flash
from werkzeug.utils import secure_filename
import os
from app import app, db
from forms import CadastroBarForm, ConsultaForm
from models import Bar
from bar import Bar as BarOperacoes
from app import app

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
	if form.validate_on_submit() and request.method == 'POST':
		filename = salvar_foto(foto=form.foto.data)
		bar.cadastra_bar(form.nome.data, form.descricao.data, form.endereco.data, form.telefone.data, form.especialidade.data, os.path.join(app.config['UPLOAD_FROM_TEMPLATES'], filename))
		flash('Bar, %s, cadastrado com sucesso!' % form.nome.data)
		form = CadastroBarForm()
	return render_template('cadastro.html', title='Cadastro', form=form)

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
	form = ConsultaForm()
	if request.method == 'POST' and form.validate_on_submit():
		filtro = form.consulta.data
		resultados = bar.consulta_bar_por_nome(filtro) 

		return render_template('consulta.html', title='Consulta', form=form, resultados=resultados, filtro=filtro)
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
		foto = result.foto
		return render_template('editar.html', title='Editar', form=form, foto=foto)
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
		if form.foto.data:
			result.foto = os.path.join(app.config['UPLOAD_FROM_TEMPLATES'], salvar_foto(foto=form.foto.data, id=result.id))
		bar.alterar_bar(result)
	return redirect(url_for('editar', id=id))
	
@app.route('/remover/<int:id>', methods=['GET', 'POST'])
def remover(id=None):
	form = CadastroBarForm()
	if id:
		rem = bar.remover_bar_por_id(id)
		if rem:
			return render_template('index.html', title='Home', message=rem.nome)
		return render_template('editar.html', title='Editar', id=id)
	return render_template('editar.html', title='Editar', form=form)