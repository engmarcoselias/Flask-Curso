from app import app
from flask import Flask, redirect, url_for,request,abort,render_template,make_response, session
from json import dumps



#======criação de rotas===================
@app.route('/')
def index():
    return 'Hello word'

@app.route('/admin/')
def admin():
    return "<h1>Admin</h1>"

@app.route('/guest/<guest>')
def guest(guest):
    return '<p>Olá <p>%s</p>'% guest

@app.route('/user/')
def user_none():
    return ''
#=====outra forma de criar uma rota======
def teste():
    return "<p>Testando</P>"

app.add_url_rule('/teste','teste',teste)

#========================================

#=======Rotas dinamicas==================

@app.route('/hello/<nome>')
def hello(nome):
    return "<h1>Hello {}</h1>".format(nome)

#======Redirecionando rotas==============

@app.route('/user/<name>')
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:    
        return redirect(url_for('guest',guest=name))
#=========================================

#========Rota para teste de metodos=======

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        return dumps(request.form)
    
    return "OK GET"
#========================================

#=====Rota para redircionamento e erro===

@app.route('/loguin',methods=['GET','POST'])
def loguin():
    if request.method =='POST':
        if request.form['username'] == 'admin' and request.form['pass'] == 'admin':
            return redirect(url_for('sucesso'), code=302)
        else:
            abort(401)
    else:
        abort(403)


@app.route('/sucesso')
def sucesso():
    return 'Sucesso'

#==Rota para templates modelo=================

@app.route('/modelo')
def modelo():
    x = 10
    y = 10
    query = request.args.to_dict()
    return render_template('modelo.html',x=x, y=y, query=query)

@app.route('/dados')
def dados():
    return render_template('dados.html')

#=====Rota exemplo dados de um templaite para outro====

@app.route('/calculo',methods=['GET','POST'])
def calculo():
    total = sum([int(v) for v in request.form.to_dict().values()])#somando usando a função sum, convertendo para inteiro um valor de string
    str(total)
    return render_template('calculo.html', total=total)

#=============Criando cookies========================

@app.route('/cookiesindex')
def cookies_index():
    return render_template('cookies.html')

@app.route('/setcookie', methods=['GET','POST'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))
    if request.method == 'POST':
        dados = request.form['c']
        resp.set_cookie('testeCookie', dados)
    return resp

@app.route('/getcookie')
def getcookies():
    cookieName = request.cookies.get('testeCookie')
    return '<h1>Valor cookie é {}</h1>'.format(cookieName)

#=======================================================

#===============Manipulando seções======================

@app.route('/sessionindex')
def session_index():
    username = ''
    if 'username' in session:
        username = session['username']
    return render_template('session.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] != '':
        session['username'] = request.form['username']
        return redirect(url_for('session_index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('session_index'))
