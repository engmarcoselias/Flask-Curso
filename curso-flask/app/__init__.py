from flask import Flask


app = Flask(__name__,static_folder='static', template_folder='templates')
app.secret_key = "123456"


from app.controllers import default




