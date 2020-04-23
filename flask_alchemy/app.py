import os

from flask import Flask, render_template, request

# Import table definitions.
from models import *

app = Flask(__name__)
# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://vfooqegoqbccjs:e04d0b9e1addba9715696c93cbfbe566bd3f56fd36fa2b72bf7a9e6272ea876b@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d92pfdtb7oefek"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
#
db.init_app(app)

def main():
  # Create tables based on each table definition in `models`
  db.create_all()

if __name__ == "__main__":
  # Allows for command line interaction with Flask application
  with app.app_context():
    main()