from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/cadastro')
def cadastro():
	return render_template('cadastro.html')

@app.route('/consulta')
def consulta():
	return render_template('consulta.html')

