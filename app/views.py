from flask import Flask, render_template
from app import app
from forms import CadastroBarForm

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/cadastro')
def cadastro():
	form = CadastroBarForm()
	return render_template('cadastro.html', form=form)

@app.route('/consulta')
def consulta():
	return render_template('consulta.html')

