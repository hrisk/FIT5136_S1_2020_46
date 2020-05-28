from flask_login import UserMixin
from . import db


class Employee(UserMixin, db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100))
    employee_title = db.Column(db.String(100))
    employee_permissions = db.Column(db.String(10000))
    employee_email = db.Column(db.String(100), unique=True)
    employee_password = db.Column(db.String(100))

    def get_id(self):
        return self.employee_id