from flask_restful import Resource, reqparse, marshal_with
from flask_injector import inject
# from fields.admin_fields_dto import resource_admin_fields
from src.api.services.admin_services import AdminServices
from src.api.services.user_services import UserServices


class LoginAdmin(Resource):
    @inject
    def __init__(self, service: AdminServices):
        self.admin_service = service

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
    parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

    def post(self):
        """
        Log admin in
        ---
        tags:
          - login
        definitions:
          - schema:
              id: Admin
              properties:
                name:
                 type: string
                 description: the admin's object
        parameters:
          - in: body
            name: body
            schema:
              id: Admin
              required:
                - email
                - password
              properties:
                email:
                  type: string
                  description: email for user
                password:
                  type: string
                  description: password for user
        responses:
          201:
            description: token created and returned
          401:
            description: error login
        """
        data = LoginAdmin.parser.parse_args()

        return self.admin_service.login_admin(data["email"], data["password"])


class LoginUser(Resource):
    @inject
    def __init__(self, service: UserServices):
        self.user_service = service

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
    parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

    def post(self):
        """
        Log user in
        ---
        tags:
          - login
        definitions:
          - schema:
              id: User
              properties:
                name:
                 type: string
                 description: the user's object
        parameters:
          - in: body
            name: body
            schema:
              id: User
              required:
                - email
                - password
              properties:
                email:
                  type: string
                  description: email for user
                password:
                  type: string
                  description: password for user
        responses:
          201:
            description: token created and returned
          401:
            description: error
        """
        data = LoginUser.parser.parse_args()

        return self.user_service.login_user(data["email"], data["password"])
