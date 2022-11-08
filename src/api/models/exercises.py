from src.api.utils.database import db


class Exercise(db.Model):
    """
    Model for exercises submitted by admins
    """
    __tablename__ = 'exercises'

    eid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    signature = db.Column(db.String(300), nullable=False)
    test_filepath = db.Column(db.String(300), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=False), nullable=False)

    def __init__(self, title, description, signature, test_filepath, timestamp):
        self.title = title
        self.description = description
        self.signature = signature
        self.test_filepath = test_filepath
        self.timestamp = timestamp
