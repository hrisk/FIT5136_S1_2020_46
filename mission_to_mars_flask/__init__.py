from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import auth
# from sqlalchemy import create_engine

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
# engine = create_engine()
# print(engine.table_names())


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/mission_to_mars'

    db.init_app(app)

    # blueprint for auth routes in our app
    import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
