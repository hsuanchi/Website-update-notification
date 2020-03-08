from datetime import datetime
from .. import db


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(10))
    insert_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, email, password):
        self.email = email
        self.password = password
