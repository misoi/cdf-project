from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

import sqlite3

app = Flask(__name__)
bcrypt = Bcrypt(app)

#config
#so that flask know which environment it is 
import os
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
from app import db



from app import views





##import os

