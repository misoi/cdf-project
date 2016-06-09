from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo

#from models import User

def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise validationError("username already exist.")

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise validationError("Email already exist.")


class RegistrationForm(Form):
    username= StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be letters,numbers and underscore only.")
                ),
            name_exists,

        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
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
