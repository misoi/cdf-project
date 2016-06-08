from app import db

class BlogPost(db.Model):
#    table name
    __tablename__ = "posts"

#columns names
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description= db.Column(db.String, nullable=False)
#    password = db.Column(db.String, nullable=False)
#    confirm= db.Column(db.String, nullable=False)

def __init__(self, title, description):

    self.title = title
    self.description = description
#    self.pasword = password
#    self.confirm = confirm

def __repr__(self):
    return '<title {}>'.format(self.title)
