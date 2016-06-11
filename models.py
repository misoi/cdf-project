from app import db

class BlogPost(db.Model):

    __tablename_ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title {}'.format(self.title)




