#set FLASK_APP=hello.py(to set the env vaiable on terminal)
#set FLASK_ENV=development to enable debug mode

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline="This is just to bother you mate!!"
	return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
	headline = "bye, come again lad"
	return render_template("bye.html", headline=headline)


#@app.route("/<string:name>")
#def hello(name):
#	return f"Hello {name}, my dear"