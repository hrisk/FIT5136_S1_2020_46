from flask import Blueprint, render_template
from mission_to_mars_flask import db

auth = Blueprint('auth', __name__, template_folder="../templates")


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return 'logged out'
