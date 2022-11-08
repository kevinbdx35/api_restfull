from src.api.utils.database import db


class GenericRepository:
    @staticmethod
    def save(element):
        db.session.add(element)
        db.session.commit()
        return element

    @staticmethod
    def find_all(obj_type):
        return db.session.query(obj_type).all()

    @staticmethod
    def find_by_id(obj_type, key_id):
        return db.session.query(obj_type).get(key_id)

    @staticmethod
    def find_by_email(obj_type, email):
        return db.session.query(obj_type).filter_by(email=email).one_or_none()
