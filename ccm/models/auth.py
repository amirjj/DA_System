from ccm.extentions import db

class User(db.Model):
	__tablename__ = "ccm_user"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique = True)
	__password = db.Column(db.String(100))
	name = db.Column(db.String(100))
	

	def __init__(self, email, name, password):
		self.name = name
		self.email = email
		self.__password = password

		

	def __repr__(self):
		return "<id {}>".format(self.id)

