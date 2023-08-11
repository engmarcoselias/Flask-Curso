from app import app
from flask import Flask, redirect, url_for,request,abort,render_template,make_response, session
from json import dumps



#======criação de rotas===================
@app.route('/')
def index():
    return 'Hello word'