from . import db
import datetime


class Mission(db.Model):
    mission_id = db.Column(db.Integer, primary_key=True)
    mission_launch_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mission_origin = db.Column(db.String(20), nullable=False)
    mission_duration = db.Column(db.Integer, nullable=False)
    mission_type = db.Column(db.String(30))
    mission_description = db.Column(db.Text, nullable=False)
    mission_employment_requirement = db.Column(db.String(100), nullable=False)
    mission_age = db.Column(db.String(10), nullable=False)
    mission_min_experience = db.Column(db.String(20), nullable=False)
    mission_qualifications = db.Column(db.String(10), nullable=False)
    mission_occupations = db.Column(db.String(30))
    mission_skills = db.Column(db.String(15), nullable=False)
    mission_language_required = db.Column(db.String(20), nullable=False)
    mission_secondary_language = db.Column(db.String(40))
    mission_cargo_for = db.Column(db.String(40), nullable=False)
    mission_cargo_required = db.Column(db.String(40))
    mission_quantity_each = db.Column(db.Integer, nullable=False)



    def get_id(self):
        return self.mission_id
