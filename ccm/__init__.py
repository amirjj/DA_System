import os

def configure_app(app, test_config):
	from ccm.config import DevelopmentConfig
	if test_config is not None:
		app.config.from_object(test_config)
	app.config.from_object(DevelopmentConfig)
	app.config.from_pyfile('environ.py')


def configure_extentions(app):
	from flask_migrate import Migrate, MigrateCommand
	from ccm.extentions import db
	
	# migrate initiated seperately as it need two parameters 
	# (in future if needed, it will be add to extentions.py)
	migrate = Migrate(app, db)
	from ccm import extentions as ex

	for extention in app.config['EXTENTIONS']:
		getattr(ex, extention).init_app(app)

def configure_blueprints(app):
	from importlib import import_module

	for package in app.config['BLUEPRINTS']:
		module_name = package[0]
		object_name = package[1]

		module_obj = import_module(module_name)
		bp = getattr(module_obj, object_name)
		app.register_blueprint(bp)
	return app


def create_app(test_config=None):
	from flask import Flask

	app = Flask(__name__)
	configure_app(app, test_config)
	configure_extentions(app)
	configure_blueprints(app)
	#configure_directories
	#configure_sentry


	return app

#this function helps if we need to run migration manually(python manage.py db ..)
#otherwise its irrelevent 
def migration_helper(test_config=None):
	from flask import Flask
	app = Flask(__name__)

	from models.auth import User

	from config import DevelopmentConfig
	if test_config is not None:
		app.config.from_object(test_config)
	app.config.from_object(DevelopmentConfig)
	app.config.from_pyfile('environ.py')
	from extentions import db
	db.init_app(app)
	return app, db



# if __name__ == "__main__":
# 	app.run()

