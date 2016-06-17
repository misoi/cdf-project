from app import db, bcrypt



class signup(db.Model):

	__tablename__= 'users'

	id =db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String,nullable=False)
	email = db.Column(db.String,nullable=False)
	password = db.Column(db.String,nullable=False)
	confirm= db.Column(db.String,nullable=False)


	def __init__(self, username, email, password, confirm):
		self.username= username
		self.email = email
		self.password= bcrypt.generate_password_hash(password)
		self.confirm= bcrypt.generate_password_hash(confirm)



	def __repr__(self):
		return '<username{}'.format(self.username)
