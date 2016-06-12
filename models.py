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


# users teble

class User(db.Model):
	__tablename_ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	confirm= db.Column(db.String, nullable=False)

	def __init__(self, name, email, password, confirm):
		self.name = name
		self.email = email
		self.password = password
		self.confirm = confirm

	def __repr__(self):
		return '<name {}'.format(self.name)

	



