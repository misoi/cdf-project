from flask_wtf import Form
from models import signup
from wtforms import TextField, PasswordField, validators
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo



#from models import User

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
