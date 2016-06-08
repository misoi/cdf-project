from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "my previous"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'


db = SQLAlchemy(app)
#from  models import signup

from app import views
