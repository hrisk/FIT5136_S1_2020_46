from . import db


class Criteria(db.Model):
    criteria_id = db.Column(db.Integer, primary_key=True)
    criteria_name = db.Column(db.String(100), unique=True, nullable=False)

    def get_id(self):
        return self.criteria_id
