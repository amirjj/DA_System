from ccm.extentions import db
from flask_login import UserMixin

class User(UserMixin ,db.Model):
	__tablename__ = "ccm_user"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique = True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(100))
	

	def __init__(self, email, name, password):
		self.name = name
		self.email = email
		self.password = password

	def __repr__(self):
		return "<id {}>".format(self.id)

