from app import app, db, bcrypt
from wtforms import TextField, PasswordField, validators, Form
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo





#should be randomly generated
app.secret_key = '9vY%N\\#l\xd1L\xd6r\xac\xec\xf5\xa6\x01W9_QD\\$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost/cynthia'


#creating tables
class Signup(db.Model):

	__tablename__= 'users'

	id =db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String,nullable=False)
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

class Apply(db.Model):

    __tablename__= 'applicants'

    fname=db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    nid = db.Column(db.String,nullable=False)
    ward= db.Column(db.String,nullable=False)
    location=db.Column(db.Integer, primary_key=True)
    slocation = db.Column(db.String,nullable=False)
    village = db.Column(db.String,nullable=False)
    college = db.Column(db.String,nullable=False)
    year= db.Column(db.String,nullable=False)


    def __init__(self,fname,sname,email,nid,ward,location,slocation,village,college,year):
        self.fname= fname
        self.sname = sname
        self.email= email
        self.nid= nid
        self.ward= ward
        self.location = location
        self.slocation = slocation
        self.village= village
        self.college= college
        self.year= year
        



    def __repr__(self):
        return '<fname{}'.format(self.fname)
#forms
def email_exists(form, field):
    if user.select().where(user.email == field.data).exists():
        raise validationError("Email already exist.")


class RegistrationForm(Form):
    username = TextField('Username', [validators.Required("Enter your name"),Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Name should be letters,numbers and underscore only.")
                ),
        ])
    email = TextField(
        'Email',
        validators=[
            DataRequired(),
            Email(message=None),
            email_exists
            ])
    password = PasswordField(
        'Password',
        validators=(
            DataRequired(),
            Length(min=4),))
    password2 = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message="passwords must match")
        ])


if __name__ == '__main__':
	

	app.run(debug=True)

