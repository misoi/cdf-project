from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)



#
db = SQLAlchemy(app)
from models import *

from app import views




##import os

