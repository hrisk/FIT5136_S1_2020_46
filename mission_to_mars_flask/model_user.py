from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required in SQLAlchemy
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    user_type = db.Column(db.Enum("Candidate", "Employee", name="user_type"), nullable=False, default="Candidate")
    # user = db.relationship("Employee", backref=db.backref("employee", uselist=False), back_populates="user")

    def get_id(self):
        return self.id
