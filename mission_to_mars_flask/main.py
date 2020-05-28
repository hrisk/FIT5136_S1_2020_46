from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint(name='main', import_name=__name__, template_folder="templates")


@main.route(rule='/')
def index():
    return render_template(template_name_or_list='index.html')


@main.route(rule='/mission-list')
@login_required
def mission_list():
    return render_template(template_name_or_list='feature1.html', name=current_user.employee_name)


@main.route(rule='/profile')
@login_required
def profile():
    return render_template(template_name_or_list='profile.html', name=current_user.employee_name)


@main.route(rule='/shuttle')
def shuttle():
    mission_list = ['Mission A', 'Mission B']
    shuttle_list = ['Shuttle A', 'Shuttle B']
    return render_template(template_name_or_list='feature2.html', mission_list=mission_list, shuttle_list=shuttle_list)


# TODO: proper error handler
@main.errorhandler(404)
def not_found(e):
    return render_template(template_name_or_list='404.html')
