from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

import os
app.secret_key= "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
#so that flask will know which environment is in
#app.config.from_object(os.environ['APP_SETTINGS'])


db = SQLAlchemy(app)


#from  models import signup

from app import views
