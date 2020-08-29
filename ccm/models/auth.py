from app import db

class User(db.Model):
	__tablename__ = "User"
	id = db.column(db.Integer, primary_key=True)
	name = db.column(db.String)
	last_name = db.column(db.String)

	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name

	def __repr__(self):
		return "<id {}>".format(self.id)

