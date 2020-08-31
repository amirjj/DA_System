from flask import Blueprint, g, render_template, abort
from jinja2 import TemplateNotFound


auth_bp = Blueprint('auth.authentication', __name__, template_folder="templates", url_prefix="/auth")


@auth_bp.route("/register")
def register():
	return "registeration"


