


class DefaultConfig(object):
	"""DefaultConfig includes common configurations for flask app.
	Other config objects inheret these common properties from it.
	"""
	pass

class ProductionConfig(DefaultConfig):
	pass

class DevelopmentConfig(DefaultConfig):
	pass

class TestingConfig(DefaultConfig):
	pass


		
		
		