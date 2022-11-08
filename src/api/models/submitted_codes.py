from src.api.utils.database import db

from datetime import datetime


class Code(db.Model):
    """
    Model for code that will be sent/submitted by developers (users)
    """
    __tablename__ = 'codes'

    cid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("users_app.uid"))
    eid = db.Column(db.Integer, db.ForeignKey("exercises.eid"))
    filepath_of_code = db.Column(db.String(300))
    hash_of_code = db.Column(db.String(300))
    coverage_score = db.Column(db.Float)
    time_stamp = db.Column(db.DateTime(timezone=True), nullable=False)

    user = db.relationship("User")
    exercise = db.relationship("Exercise")

    def __init__(self, uid, eid, filepath, digest):
        self.uid = uid
        self.eid = eid
        self.filepath_of_code = filepath
        self.hash_of_code = digest
        self.coverage_score = "0"
        self.time_stamp = datetime.now()

    # Put this in service
    # def hashfile_control(self, filepath):
    #     hash1 = self.hash_of_code
    #     hash2 = self.hashfile(filepath)
    #     return hash1 == hash2
