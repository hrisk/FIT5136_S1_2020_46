from . import db
import datetime


class Shuttle(db.Model):
    shuttle_id = db.Column(db.Integer, primary_key=True)
    shuttle_name = db.Column(db.String(100), unique=True, nullable=False)
    shuttle_manufacture_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    shuttle_fuel_capacity = db.Column(db.Integer, nullable=False)
    shuttle_passenger = db.Column(db.Integer, nullable=False)
    shuttle_cargo_capacity = db.Column(db.Integer, nullable=False)
    shuttle_speed = db.Column(db.Integer, nullable=False)
    shuttle_origin = db.Column(db.String(100), nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey('Mission.mission_id'), nullable=False)
    mission = db.relationship("User", backref=db.backref("Mission", uselist=False))

    def get_id(self):
        return self.shuttle_id