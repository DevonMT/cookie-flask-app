from sys import argv

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from views.home import home

config_filename = argv[1] or "prod_settings.cfg"

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_file=config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        app.register_blueprint(home)

        return app


if __name__ == "__main__":
    create_app().run()
