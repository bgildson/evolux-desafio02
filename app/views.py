from flask import Flask, render_template
from app import app
from forms import CadastroBarForm, ConsultaForm
from daoDB import DaoDB

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	form = CadastroBarForm()
	if form.validate_on_submit():
		pass
	return render_template('cadastro.html', title='Cadastro', form=form)

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
	form = ConsultaForm()
	resultados = [{'nome': 'Gildson Bezerra da Silva', 'descricao': 'Sem descricao', 'endereco': 'Sem endereco', 'telefone': 'Sem telefones', 'especialidade': 'Sem especialidade'},
				 {'nome': 'Genilson Bezerra', 'descricao': 'Sem nenhuma descricao', 'endereco': 'Sem nenhum endereco', 'telefone': 'Sem nenhum telefone', 'especialidade': 'Sem nenhuma especialidade'}]
	return render_template('consulta.html', title='Consulta', form=form, resultados=resultados, filtro='todos')

