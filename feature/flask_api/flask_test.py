from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Welcome to Python Flask Server</h1>";

@app.route("/<string:name>")
def hello_world(name):
    return f"<p>Hello {escape(name)} from Flask</p>";

@app.route("/id/<int:id>", methods=["POST"])
def id_page(id:int):
    return f'<p> added 1 to id : {escape(id+1)}</p>';