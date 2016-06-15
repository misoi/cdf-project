from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sqlite3

app = Flask(__name__)
app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'


db = SQLAlchemy(app)


from app import views





##import os

