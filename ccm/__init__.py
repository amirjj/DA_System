import os
from flask import Flask
from config import DevelopmentConfig
from models.auth import User
from extentions import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config.from_pyfile("environ.py")
db.init_app(app)

if __name__ == "__main__":
	app.run()

