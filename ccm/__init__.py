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
	from ccm import extentions as ex

	for extention in app.config['EXTENTIONS']:
		getattr(ex, extention).init_app(app)

def configure_blueprints(app):
	from ccm.blueprints.portal import dashboard
	from ccm.blueprints.auth import authentication

	for package in app.config['BLUEPRINTS']:
		if 'authentication' in package:
			bp = getattr(authentication, app.config['BLUEPRINTS']['authentication'])
			app.register_blueprint(bp)
		elif 'dashboard' in package:
			bp = getattr(dashboard, app.config['BLUEPRINTS']['dashboard'])
			app.register_blueprint(bp)
		

		

def create_app(test_config=None):
	from flask import Flask
	app = Flask(__name__)
	configure_app(app, test_config)
	configure_extentions(app)
	configure_blueprints(app)
	#configure_directories
	#configure_sentry


	return app



# if __name__ == "__main__":
# 	app.run()

