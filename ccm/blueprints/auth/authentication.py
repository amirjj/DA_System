from flask import Blueprint, request, g, render_template, abort, flash, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ccm.extentions import login_manager, db
from ccm.models.auth import User

auth_bp = Blueprint('auth.authentication', __name__, template_folder="templates", url_prefix="/auth")

@login_manager.user_loader
def user_loader(user_id):
	return User.get(user_id)

@auth_bp.route("/register", methods=('GET','POST'))
def register():
	if request.method == 'POST':
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')
		accpass = request.form.get('accpass')
		error = None
		user = User.query.filter_by(email = email).first()
		if user:
			error = 'Username already exists'
		if password != accpass:
			error = 'Passwords don\'t match'

		if error:
			flash(error)
			return redirect(url_for('auth.authentication.register'))
		#Check if password and accpass are different
		new_user = User(email=email, name=username, password=\
			generate_password_hash(password,method='sha256'))

		db.session.add(new_user)
		db.session.commit()

		return redirect(url_for('portal.dashboard.index'))

	return render_template("signup.html")

@auth_bp.route("/login", methods=('GET','POST'))
def login():
	form = LoginForm()
	if form.validate_on_submit():
		login_user(user)
		flash("Logged in successfully")
		next = request.args.get('next')
		if not is_safe_url(next):
			abort(400)
		return redirect(next or url_for(auth_bp.index))
	return render_template("login.html", form=form)

@auth_bp.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

