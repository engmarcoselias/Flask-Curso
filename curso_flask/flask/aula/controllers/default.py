from aula import app


@app.route("/")
def index():
    return "Hello Word"
