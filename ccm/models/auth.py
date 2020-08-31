from ccm.extentions import db

class User(db.Model):
	__tablename__ = "ccm_user"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique = True)
	password = db.Column(db.String(100))
	name = db.Column(db.String)
	

	def __init__(self, name, last_name):
		self.name = name
		

	def __repr__(self):
		return "<id {}>".format(self.id)

