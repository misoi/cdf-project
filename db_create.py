from app import db
from models import BlogPost

# create database

db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

# commit the changes
db.session.commit()
