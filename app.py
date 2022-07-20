from flask import Flask
app = Flask(__name__)

from professores import rotas


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

