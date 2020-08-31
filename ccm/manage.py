import os 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from extentions import db
from config import DevelopmentConfig

from __init__ import migration_helper
app, db = migration_helper(DevelopmentConfig)


manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
	manager.run()
