from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .model_mission import Mission
from .model_shuttle import Shuttle
from .model_candidate import Candidate
from .model_user import User
from .model_employee import Employee

main = Blueprint(name='main', import_name=__name__, template_folder="templates")


@main.route(rule='/')
def index():
    return render_template(template_name_or_list='index.html')


@main.route(rule='/mission-list')
@login_required
def mission_list():
    mission_details = Mission.query.all()
    return render_template(template_name_or_list='feature1.html', name=current_user.name,
                           mission_details=mission_details)


@main.route(rule='/profile')
@login_required
def profile():
    return render_template(template_name_or_list='profile.html', name=current_user.name)


@main.route(rule='/shuttle/')
def shuttle():
    mission_list = Mission.query.all()
    shuttle_details = Shuttle.query.all()
    return render_template(template_name_or_list='feature2.html', mission_list=mission_list,
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
