from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint(name='main', import_name=__name__, template_folder="templates")


@main.route(rule='/')
def index():
    return render_template(template_name_or_list='index.html')


@main.route(rule='/mission-list')
@login_required
def mission_list():
    mission_details = [{'name': 'Krishna'}]
    return render_template(template_name_or_list='feature1.html', name=current_user.name,
                           mission_details=mission_details)


@main.route(rule='/profile')
@login_required
def profile():
    return render_template(template_name_or_list='profile.html', name=current_user.employee_name)


@main.route(rule='/shuttle/')
def shuttle():
    mission_list = ['Mission A', 'Mission B', 'Mission C']
    shuttle_list = ['Shuttle A', 'Shuttle B', 'Shuttle C']
    shuttle_details = {}
    return render_template(template_name_or_list='feature2.html', mission_list=mission_list, shuttle_list=shuttle_list,
                           shuttle_details=shuttle_details)


@main.route(rule='/create-mission')
def create_mission():
    coords = [{}]
    cargo_list = [{}]
    return render_template(template_name_or_list='add_mission.html', coords=coords, cargo_list=cargo_list)


@main.route(rule='/add-criteria')
def add_criteria():
    col_list = []
    return render_template(template_name_or_list='feature3_addNewCri.html', col_list=col_list)


@main.route(rule='/candidate-list')
def candidate_list():
    return render_template(template_name_or_list='feature5.html')


@main.route(rule='/selection-criteria')
def criteria_selection():
    medical = [{}]
    criminal = [{}]
    return render_template(template_name_or_list='feature3_criteria_selection.html', medical=medical, criminal=criminal)

# TODO: proper error handler
@main.errorhandler(404)
def not_found(e):
    return render_template(template_name_or_list='404.html')
