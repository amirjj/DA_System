from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

dash_bp = Blueprint("portal.dashboard", __name__, template_folder="templates")

@dash_bp.route("/")
def index():
	return render_template("base.html", title="test")

