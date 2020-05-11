from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('SFIA1_DB_URI')
db = SQLAlchemy(app)

from application import routes
