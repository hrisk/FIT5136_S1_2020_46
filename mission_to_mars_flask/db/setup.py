from mission_to_mars_flask import db, create_app
# from . import db, create_app

db.create_all(app=create_app())
