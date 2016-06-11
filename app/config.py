#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = ''\xd4yYI\xe7\xe8\xa46$)U\xc0\x8d\xed\xd6\x89M\x0eZ\xe7\x01,a\x81''
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False 
		