from flask import Blueprint, request, g, render_template, abort, flash, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import login_user, logout_user
from ccm.extentions import login_manager
from ccm.models.auth import User

auth_bp = Blueprint('auth.authentication', __name__, template_folder="templates", url_prefix="/auth")

@login_manager.user_loader
def user_loader(user_id):
	return User.get(user_id)

@auth_bp.route("/register")
def register():
	return "registeration"

@auth_bp.route("/login", methods=['GET','POST'])
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

