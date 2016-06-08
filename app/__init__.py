from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

import os

#so that flask will know which environment is in
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

#from  models import signup

from app import views
