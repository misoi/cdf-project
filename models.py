from app import app
from wtforms import PasswordField
from flask_bcrypt import generate_password_hash

from flask_login import UserMixin
import peewee


from peewee import *


# =================config=======================
# should be randomly generated
app.secret_key = '9vY%N\\#l\xd1L\xd6r\xac\xec\xf5\xa6\x01W9_QD\\$'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/cynthia'

DATABASE = peewee.PostgresqlDatabase('cynthia', user="postgres")


# ===============================regitsration tables/shemas=====================
class User(UserMixin, Model):
    name = CharField(max_length=200)
    email = CharField(unique=True, max_length=150)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls,name, email,password):
        try:
            cls.create(
                name=name,
                email=email,
                password=generate_password_hash(password)
            )

        except IntegrityError:
            raise ValueError('user already exists')


class Personal(UserMixin, Model):
    fname= CharField(max_length=200)
    sname = CharField(max_length=200)
    email = CharField(unique=True, max_length=150)
    nid = IntegerField(primary_key=True, unique=True)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls,fname, sname, email,nid):
        try:
            cls.create(
                fname=fname,
                sname=sname,
                email=email,
                nid=nid
            )
        except IntegrityError:
            raise ValueError('Details already exists')


class Place(UserMixin, Model):
    county = CharField(max_length=150)
    constituency = CharField( max_length=150)
    ward= CharField(max_length=50)
    location= CharField(max_length=50)
    slocation = CharField(max_length=50)
    village = CharField(max_length=50)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, county, constituency, ward, location, slocation, village):
        try:
            cls.create(
                county=county,
                constituency=constituency,
                ward=ward,
                location=location,
                slocation=slocation,
                village=village
            )


        except IntegrityError:
            raise ValueError('Details already exists')


class School(UserMixin, Model):
    college = CharField(max_length=50)
    year= CharField()

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, college, year):
        try:
            cls.create(
                college=college,
                year=year
            )


        except IntegrityError:
            raise ValueError('Details already exists')


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User,Personal,Place,School], safe=True)
    DATABASE.close()




