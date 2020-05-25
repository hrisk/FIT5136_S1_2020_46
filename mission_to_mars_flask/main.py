from flask import Blueprint, render_template
from mission_to_mars_flask import db

main = Blueprint('main', __name__, template_folder="../templates")


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')
