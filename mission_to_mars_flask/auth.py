from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
# from .models import User
from .model_employee import Employee
from . import db

auth = Blueprint(name="auth", import_name=__name__, template_folder="templates")


@auth.route(rule='/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = Employee.query.filter_by(employee_email=email).first()

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.employee_password, password):
            flash(message='Please check your login details and try again')
            return redirect(
                location=url_for(endpoint='auth.login'))  # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user=user, remember=remember)
        return redirect(location=url_for(endpoint='main.profile'))

    return render_template(template_name_or_list='login.html')


# @auth.route(rule="/login", methods=['POST'])
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     remember = True if request.form.get('remember') else False
#
#     user = User.query.filter_by(email=email).first()
#
#     # check if user actually exists
#     # take the user supplied password, hash it, and compare it to the hashed password in database
#     if not user or not check_password_hash(user.password, password):
#         flash(message='Please check your login details and try again')
#         return redirect(
#             location=url_for(endpoint='auth.login'))  # if user doesn't exist or password is wrong, reload the page
#
#     # if the above check passes, then we know the user has the right credentials
#     login_user(user=user, remember=remember)
#     return redirect(location=url_for(endpoint='main.profile'))


@auth.route(rule='/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = Employee.query.filter_by(
            employee_email=email).first()  # if this returns a user, then the email already exists in database
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            flash(message="Email address already exists")
            return redirect(location=url_for(endpoint='auth.signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = Employee(employee_email=email,
                            employee_name=name,
                            employee_password=generate_password_hash(password, method="sha256"),
                            employee_title="Admin",
                            employee_permissions="none")

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(location=url_for(endpoint='auth.login'))

    return render_template(template_name_or_list='signup.html')


# @auth.route(rule='/signup', methods=['POST'])
# def signup_post():
#     email = request.form.get('email')
#     name = request.form.get('name')
#     password = request.form.get('password')
#
#     user = User.query.filter_by(
#         email=email).first()  # if this returns a user, then the email already exists in database
#     if user:  # if a user is found, we want to redirect back to signup page so user can try again
#         flash(message="Email address already exists")
#         return redirect(location=url_for(endpoint='auth.signup'))
#
#     # create new user with the form data. Hash the password so plaintext version isn't saved.
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))
#
#     # add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()
#
#     return redirect(location=url_for(endpoint='auth.login'))


@auth.route(rule='/logout')
@login_required
def logout():
    logout_user()
    return redirect(location=url_for(endpoint='main.index'))
