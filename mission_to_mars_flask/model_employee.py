from . import db
from .model_user import User


class Employee(db.Model):
    __tablename__ = "employee"
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_title = db.Column(db.String(100), nullable=False)
    employee_permissions = db.Column(db.String(10000), nullable=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("user", uselist=False))

    def get_id(self):
        return self.employee_id