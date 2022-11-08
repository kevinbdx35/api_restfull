from src.api.utils.database import db


class Admin(db.Model):
    """
    Model for Admin
    """
    __tablename__ = 'admin_app'

    rid = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, email, password):  # last_name, first_name,
        # self.last_name = last_name
        # self.first_name = first_name
        self.email = email
        self.password = password
