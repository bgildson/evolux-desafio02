# -*- coding: cp1252 -*-
from flask import Flask, render_template, redirect, request
from . import app
from forms import CadastroBarForm, ConsultaForm
from daoDB import DaoDB

dao = DaoDB()

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	form = CadastroBarForm()
	if form.validate_on_submit():
		print('alguma coisa')
		print(form.nome.data)
		pass
	return render_template('cadastro.html', title='Cadastro', form=form)

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
	form = ConsultaForm()
	if request.method == 'POST' and form.validate_on_submit():
		filtro = form.consulta.data
		#dao.open()
		resultados = dao.consulta_bar_geral(filtro)
		#dao.close()
		#resultados = [{'nome': 'Gildson Bezerra da Silva', 'descricao': 'Sem descricao', 'endereco': 'Sem endereco', 'telefone': 'Sem telefones', 'especialidade': 'Sem especialidade'}, 					  {'nome': 'Genilson Bezerra', 'descricao': 'Sem nenhuma descricao', 'endereco': 'Sem nenhum endereco', 'telefone': 'Sem nenhum telefone', 'especialidade': 'Sem nenhuma especialidade'}]
		return render_template('consulta.html', title='Consulta', form=form, resultados=resultados, filtro=filtro)
	return render_template('consulta.html', title='Consulta', form=form)

