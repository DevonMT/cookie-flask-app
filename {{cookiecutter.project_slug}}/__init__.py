from flask import Flask
from flask_bootstrap import Bootstrap

from views.home import home


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.cfg")

    Bootstrap(app)

    app.register_blueprint(home)
    return app


if __name__ == "__main__":
    create_app().run()
