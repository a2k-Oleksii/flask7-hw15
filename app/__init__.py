import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migration = Migrate()


def create_app(envoiroment="developement"):
    from config import config
    from app.view import auth_blueprint, main_blueprint, plant_blueprint
    from app.models import User, AnonymousUser, Plant

    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", envoiroment)
    app.config.from_object(config[env])
    config[env].configure(app)

    db.init_app(app)
    migration.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(plant_blueprint)

    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.anonymous_user = AnonymousUser

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code

    return app
