



class DefaultConfig(object):
	"""DefaultConfig includes common configurations for flask app.
	Other config objects inheret these common properties from it.
	"""
	DEBUG = False
	TESTING = False
	DB_SERVER = "127.0.0.1"
	SECRET_KEY = "dev"
	
	# @property
	# def DATABASE_URI(self):
	# 	return 'mysql://user@{}/foo'.format(self.DB_SERVER)
	

class ProductionConfig(DefaultConfig):
	pass

class DevelopmentConfig(DefaultConfig):
	DEBUG = True
	

class TestingConfig(DefaultConfig):
	DEBUG = True
	


		
		