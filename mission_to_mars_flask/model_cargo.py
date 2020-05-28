from . import db


class Cargo(db.Model):
    cargo_id = db.Column(db.Integer, primary_key=True)
    cargo_name = db.Column(db.String(100), unique=True, nullable=False)
    cargo_quantity = db.Column(db.Integer, nullable=False)


    def get_id(self):
        return self.cargo_id