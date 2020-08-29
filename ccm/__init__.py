import os
from ccm.models.auth import User


def configure_app(app, test_config):
	from ccm.config import DevelopmentConfig
	app.config.from_object(DevelopmentConfig)
	if test_config is not None:
		app.config.from_mapping(test_config)
	app.config.from_pyfile('environ.py')


def configure_extentions(app):
	from ccm.extentions import db
	import ccm.extentions as ex

	for extention in app.config['EXTENTIONS']:
		getattr(ex, extention).init_app(app)


def create_app(test_config=None):
	from flask import Flask
	app = Flask(__name__)
	configure_app(app, test_config)
	configure_extentions(app)
	#configure_blueprints
	#configure_directories
	#configure_sentry


	return app



# if __name__ == "__main__":
# 	app.run()

