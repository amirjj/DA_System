from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

dash_bp = Blueprint("portal.dashboard", __name__, template_folder="templates")

@dash_bp.route("/")
@login_required
def index():
	return render_template("index.html", title='CCM')

