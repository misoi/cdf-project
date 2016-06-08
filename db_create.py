from app import db
from models import BlogPost

#create database and table
db.create_all()

#insert data ti the database
db.session.add(BlogPost("Good", "i\'m good."))
db.session.add(BlogPost("hahaha.", "i'm well"))


#commit

db.session.commit()



