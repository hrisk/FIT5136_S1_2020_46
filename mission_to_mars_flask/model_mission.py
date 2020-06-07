from . import db
from .model_employee import Employee
from .model_shuttle import Shuttle


class Mission(db.Model):
    __tablename__ = "mission"
    mission_id = db.Column(db.Integer, primary_key=True)
    mission_name = db.Column(db.String(100), unique=True, nullable=False)
    mission_description = db.Column(db.Text, nullable=True)
    mission_origin_country = db.Column(db.String(100), nullable=False)
    mission_countries_allowed = db.Column(db.String(1000), nullable=True)

    mission_coordinator_id = db.Column("mission_coordinator_id", db.Integer, db.ForeignKey("employee.employee_id"),
                                       nullable=False)
    employee = db.relationship("Employee", backref=db.backref("employee", uselist=False))

    mission_employment_requirement = db.Column(db.String(1000), nullable=True)
    mission_cargo_requirements = db.Column(db.String(1000), nullable=True)

    mission_launch_date = db.Column(db.DateTime, nullable=True)
    mission_location = db.Column(db.String(1000), nullable=True)
    mission_duration = db.Column(db.Integer, nullable=True)
    mission_status = db.Column(
        db.Enum("Planning Phase", "Departed Earth", "Landed on Mars", "Mission in progress", "Returned to Earth",
                "Mission Completed", name="mission_status"), nullable=False, default="Planning Phase")
    mission_shuttle_id = db.Column("mission_shuttle_id", db.Integer, db.ForeignKey("shuttle.shuttle_id"))
    shuttle = db.relationship("Shuttle", backref=db.backref("shuttle", uselist=False))

    def get_id(self):
        return self.mission_id
