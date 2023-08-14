from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite3"
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()



