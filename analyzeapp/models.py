from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class Recent(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    chart = db.Column(db.String())

    def __init__(self, chart):
        self.chart = chart

class Setting(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    recent_num = db.Column(db.Integer())
    reload_last = db.Column(db.Boolean())

    def __init__(self,recent_num,reload_last):
        self.recent_num = recent_num
        self.reload_last = reload_last
