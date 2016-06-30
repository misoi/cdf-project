from flask_wtf import Form 
from wtforms import TextField, PasswordField 
from wtforms.validators import DataRequired, Length, Email, EqualTo
#forms




        # ==========================login wtf form====================

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired('input your username')])
    password = PasswordField('Password', validators=[DataRequired('input your password')])

    #============================================== RegistrationForm form========================================================================
# def email_exists(form, field):
#     if user.select().where(user.email == field.data).exists():
#         raise validationError("Email already exist.")
       
class RegistrationForm(Form):
    username = TextField('Username', validators=[DataRequired("Enter your name")
                
        ])
    email = TextField(
        'Email',
        validators=[
            DataRequired(),
            Email(message="Valid email is required")
            ])
    password = PasswordField(
        'Password',
        validators=(
            DataRequired(),
            Length(min=4),))
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message="passwords must match")
        ])
