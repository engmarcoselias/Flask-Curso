from app import app

#---------Definindo rotas--------------

@app.route("/index")
@app.route("/")
def index():
    return "Inicio"

#--------passando parametros----------------
@app.route("/test", defaults={'name': None})
#@app.route("/test/")
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá usuario!"