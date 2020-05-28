from flask_login import UserMixin
from . import db


# TODO: finish the candidate model and add the relevant columns in database
class Candidate(UserMixin, db.Model):
    candidate_id = db.Column(db.Integer, primary_key=True)
    candidate_name = db.Column(db.String(100))
    candidate_email = db.Column(db.String(100), unique=True)
    candidate_password = db.Column(db.String(100))

    def get_id(self):
        return self.candidate_id
