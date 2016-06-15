from app import db
from models import signup


# create database

db.create_all()

# insert data
db.session.add(signup("cynthia", "cynthia@gmail.com", "chepkemoi@23", "chepkemoi@23"))
db.session.add(signup("mercy", "cmercy@gmail.com", "chepkemoi@23", "chepkemoi@23"))
db.session.add(signup("john", "john@gmail.com", "chepkemoi@23", "chepkemoi@23"))
db.session.add(signup("mathew", "mathew@gmail.com", "chepkemoi@23", "chepkemoi@23"))

# commit the changes
db.session.commit()
