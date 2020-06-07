from . import db
import datetime


class Shuttle(db.Model):
    __tablename__ = "shuttle"
    
    shuttle_id = db.Column(db.Integer, primary_key=True)
    shuttle_name = db.Column(db.String(100), unique=True, nullable=False)
    shuttle_manufacture_year = db.Column(db.Integer, nullable=True)
    shuttle_fuel_capacity = db.Column(db.Integer, nullable=True)
    shuttle_passenger_capacity = db.Column(db.Integer, nullable=True)
    shuttle_cargo_capacity = db.Column(db.Integer, nullable=True)
    shuttle_speed = db.Column(db.Integer, nullable=True)

    def get_id(self):
        return self.shuttle_id
