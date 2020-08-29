from extentions import db

class User(db.Model):
	__tablename__ = "ccm_user"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	last_name = db.Column(db.String)
	addres = db.Column(db.String)

	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name

	def __repr__(self):
		return "<id {}>".format(self.id)

