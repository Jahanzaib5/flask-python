import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	rightnow = datetime.datetime.now()
	headline = (rightnow.month == 1 and rightnow.day==1)
	return render_template("index.html", headline=headline)