from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,static_folder='static', template_folder='templates')
db = SQLAlchemy(app)
app.secret_key = "123456"


from app.controllers import default




