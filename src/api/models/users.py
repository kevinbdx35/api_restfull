from src.api.utils.database import db


class User(db.Model):
    """
    Model for simple User
    """
    __tablename__ = 'users_app'

    uid = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(300))
    password = db.Column(db.String(300))

    def __init__(self, last_name, first_name, email, password):
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password = password
