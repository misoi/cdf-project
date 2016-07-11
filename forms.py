from flask_wtf import Form

from wtforms import StringField, PasswordField, IntegerField, FileField
from wtforms.validators import (DataRequired, Regexp, Email,
                                Length, EqualTo, ValidationError)
from models import User



        # ==========================login wtf form====================


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired('input your username'), Email()])
    password = PasswordField('Password', validators=[DataRequired('input your password')])

    #================================== RegistrationForm form================


def name_exists(form, field):
    if User.select().where(User.name == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')


class RegisterForm(Form):
    name = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[ a-zA-Z0-9_]+$',
                message=("username should be one word, letters, "
                         " numbers, andd underscores only")
            ),
            name_exists])

    email = StringField(

        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Password must match')]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()])


    #applicatnts form
class DetailForm(Form):
    fname = StringField(
        'First name',
        validators=[
            DataRequired()]
    )
    sname= StringField(
        'Second name',
        validators=[
            DataRequired()]
    )
    email= StringField(
        'Valid email',
        validators=[
            DataRequired()]
    )
    nid= IntegerField(
        'Your national id number',
        validators=[
            DataRequired()]
    )


class PlacedetailForm(Form):
    county = StringField(
        'Your county',
        validators=[
            DataRequired()]
    )
    constituency = StringField(
        'Your constituency',
        validators=[
            DataRequired()]
    )
    ward = StringField(
        'Your ward',
        validators=[
            DataRequired()]
    )
    location = StringField(
        'Your home location',
        validators=[
            DataRequired()]
    )
    slocation = StringField(
        'Home sub-location',
        validators=[
            DataRequired()]
    )
    village = StringField(
        'Home village',
        validators=[
            DataRequired()]
    )


class SchooldetailForm(Form):
    college=StringField(
        'Your current college or school',
        validators=[
            DataRequired()]
    )
    year= StringField(
        'Your year of study',
        validators=[
            DataRequired()]
    )