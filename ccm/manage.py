import os 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from __init__ import app, db
from config import DevelopmentConfig


app.config.from_object(DevelopmentConfig)
app.config.from_pyfile("environ.py")

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
	manager.run()
