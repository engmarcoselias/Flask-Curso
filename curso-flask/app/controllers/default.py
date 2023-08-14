from app import app
from flask import Flask



#======criação de rotas===================
@app.route('/')
def index():
    return 'Hello word'