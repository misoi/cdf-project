import os
class  BaseConfig(object):
	DEBUG = False
	#should be randomly generated
	SECRET_KEY = '9vY%N\\#l\xd1L\xd6r\xac\xec\xf5\xa6\x01W9_QD\\$'
	SQLALCHEMY_DATABASE_URI = os.environ['postgres://postgres:postgres@localhost/cynthia']

#configuration for different environment

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False