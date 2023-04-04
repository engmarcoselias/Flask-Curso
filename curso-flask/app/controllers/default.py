from app import app
from flask import Flask, redirect, url_for



#======criação de rotas======
@app.route('/')
def index():
    return 'Hello word'

@app.route('/admin/')
def admin():
    return "<h1>Admin</h1>"

@app.route('/guest/<guest>')
def guest(guest):
    return '<p>Olá <p>%s</p>'% guest

def teste():
    return "<p>Testando</P>"

app.add_url_rule('/teste','teste',teste)

#============================

#=======Rotas dinamicas======

@app.route('/hello/<nome>')
def hello(nome):
    return "<h1>Hello {}</h1>".format(nome)

#======Redirecionando rotas===

@app.route('/user/<name>')
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:    
        return redirect(url_for('guest',guest=name))
