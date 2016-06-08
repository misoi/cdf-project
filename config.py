import os
#default config

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xa0^\xd1\xa3\xecC\x920\x8c\xa4\xb0-\xf8\x88|\xb3\x95b\xdfn\t\x19[\xa0'

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
