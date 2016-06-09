from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key= "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
#
db = SQLAlchemy(app)
from app import views




##import os


#
#from app import views
#
