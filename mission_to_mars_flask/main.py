from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint(name='main', import_name=__name__, template_folder="templates")


@main.route(rule='/')
def index():
    return render_template(template_name_or_list='index.html')


@main.route(rule='/profile')
@login_required
def profile():
    return render_template(template_name_or_list='profile.html', name=current_user.name)


# TODO: proper error handler
@main.errorhandler(404)
def not_found(e):
    return render_template(template_name_or_list='404.html')

