from flask_login import UserMixin
from . import db


class Mission(db.Model):
    mission_id = db.Column(db.Integer, primary_key=True)
    mission_name = db.Column(db.String(100))

    def get_id(self):
        return self.mission_id
