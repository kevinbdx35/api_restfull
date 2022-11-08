from flask_jwt_extended import create_access_token  # , create_refresh_token
from src.api.models.users import User
from src.api.repositories.user_repository import UserRepository
from src.api.utils.cryptography import bcrypt


class UserServices:
    def __init__(self):
        self.repository = UserRepository()

    def save_user(self, last_name, first_name, email, password):
        pw_hash = bcrypt.generate_password_hash(password)
        pw_hash_decode = pw_hash.decode("utf-8")
        return self.repository.save(User(last_name, first_name, email, pw_hash_decode))

    def login_user(self, email, password):
        user = self.repository.find_by_email(User, email)
        if user is not None:
            if bcrypt.check_password_hash(user.password, password):
                access_token = create_access_token(identity=user.uid, additional_claims={"role": "user"}, fresh=True)
                # refresh_token = create_refresh_token(user.uid)
                return {'access_token': access_token}, 200
        else:
            return {"message": "wrong user or password"}, 401
