from flask import Flask, render_template
from app import app
from forms import CadastroBarForm

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

@app.route('/consulta')
def consulta():
	return render_template('consulta.html', title='Consulta')

