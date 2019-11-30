from flask import Flask
from flask-bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    config(app)
    init_extensions(app)
    register_blueprints(app)
    return app


def init_extensions(app):
    Bootstrap(app)


def register_blueprints(app):
    from .views.home import home

    app.register_blueprints(home)


def config(app):
    app.config.from_pyfile("settings.py")
    app.config.from_envvar("{{cookiecutter.project_slug.upper()}}_SETTINGS}}")


if __name__ == "__main__":
    create_app().run()
