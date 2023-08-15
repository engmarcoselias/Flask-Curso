from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storage.db"

db = SQLAlchemy(app)

from  app.model import table

with app.app_context():
        db.create_all()
    






