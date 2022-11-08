from flask_jwt_extended import create_access_token  # , create_refresh_token
from src.api.repositories.admin_repository import AdminRepository
from src.api.models.admin import Admin
from src.api.utils.cryptography import bcrypt


class AdminServices:
    def __init__(self):
        self.repository = AdminRepository()

    def create_admin(self):
        email = 'admin@admin.com'
        password = 'admin'
        pw_hash = bcrypt.generate_password_hash(password)
        pw_hash_decode = pw_hash.decode('utf-8')
        admin = Admin(email, pw_hash_decode)
        return self.repository.save(admin)

    def login_admin(self, email, password):
        admin = self.repository.find_by_email(Admin, email)
        if admin is not None:
            # Check hash password
            if bcrypt.check_password_hash(admin.password, password):
                access_token = create_access_token(identity=admin.rid, fresh=True)
                return {'access_token': access_token}, 200
        else:
            return {"message": "Wrong admin or password"}, 401
