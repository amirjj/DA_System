import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config.from_pyfile("environ.py")
db = SQLAlchemy(app)


if __name__ == "__main__":
	app.run()

