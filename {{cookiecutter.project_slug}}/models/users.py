from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class User(UserMixin, db.Model):
    __tablename__ = "flasklogin-users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False, unique=False)
    last_name = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(200), primary_key=False, nullable=False, unique=False)
    created_on = db.Column(db.DateTime, index=False, nullable=True, unique=False)
    last_login = db.Column(db.DateTime, index=False, nullable=True, unique=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"
