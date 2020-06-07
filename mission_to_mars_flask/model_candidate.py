from . import db
from flask_login import UserMixin
from datetime import datetime


# id    name      dateofbirth     street  city    postal  country     phone
# identificationtype  gender  allergies   foodpreferences     qualifications
# yearsofworkexperience   occupation  computerskills    languagesknown
# TODO: finish the candidate model and add the relevant columns in database
class Candidate(db.Model):
    __tablename__ = "candidate"
    candidate_id = db.Column(db.Integer, primary_key=True)
    candidate_dob = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    candidate_phone = db.Column(db.String(20), unique=True, nullable=False)
    candidate_identification_type = db.Column(db.String(10), nullable=False)
    candidate_gender = db.Column(db.String(10), nullable=False)
    candidate_allergies = db.Column(db.String(20), nullable=False)
    candidate_food_preference = db.Column(db.String(20), nullable=False)
    candidate_qualification = db.Column(db.String(20))
    candidate_experience = db.Column(db.String(20))
    candidate_occupation = db.Column(db.String(50))
    candidate_computer_skills = db.Column(db.String(30), nullable=False)
    candidate_languages_known = db.Column(db.String(100), nullable=False)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    # user_relationship = db.relationship("User", backref=db.backref("user", uselist=False))

    def get_id(self):
        return self.candidate_id
