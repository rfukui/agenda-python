from flask import Flask
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/professores/")
def get():
    return "<p>Hello, World!</p>"

@app.route("/professores/")
def put():
    return "<p>Hello, World!</p>"

@app.route("/professores/")
def delete():
    return "<p>Hello, World!</p>"

