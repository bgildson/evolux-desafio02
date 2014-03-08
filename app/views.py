# -*- coding: cp1252 -*-
from flask import Flask, render_template, redirect, request, url_for, flash
from werkzeug.utils import secure_filename
from app import app, db
from forms import CadastroBarForm, ConsultaForm
from models import Bar
from bar import Bar as BarOperacoes
from app import app

bar = BarOperacoes()

def get_extension(name):
	return name.rsplit('.', 1)[1]

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	form = CadastroBarForm()
	if form.validate_on_submit() and request.method == 'POST':
		filename = ''
		if form.foto.data:
			foto = form.foto.data
			filename = secure_filename(form.foto.data.filename)
			if bar.last():
				filename = str(int(bar.last().id) + 1) + '.' + get_extension(filename)
			else:
				filename = '1.' + get_extension(filename)
			foto.save(app.config['FOTO_URI_FROM_PATH'] + filename)
			foto.close()
		else:
			filename = app.config['FOTO_PADRAO_BAR']
		bar.cadastra_bar(form.nome.data, form.descricao.data, form.endereco.data, form.telefone.data, form.especialidade.data, app.config['FOTO_URI_FROM_TEMPLATES'] + filename)
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
	print id
	form = CadastroBarForm()
	result = bar.consulta_bar_por_id(id)
	print 'ok1'
	if result:
		print 'ok2'
		form.id.data = result.id
		form.nome.data = result.nome
		form.descricao.data = result.descricao
		form.endereco.data = result.endereco
		form.telefone.data = result.telefone
		form.especialidade.data = result.especialidade
		print 'ok3'
		foto = result.foto
		print 'ok4'
		return render_template('index.html', title='Editar', form=form, foto=foto)
	return redirect( url_for('home') )
	
@app.route('/remover/<int:id>', methods=['GET', 'POST'])
def remover(id):
	print 'Novo ID: ' + str(id)
	if id:
		removido = bar.remover_bar_por_id(id)
		return render_template('index.html', title='Home', message=removido.nome)
	return render_template('index.html', title='Home')



