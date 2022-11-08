from flask_restful import Resource, reqparse, marshal_with
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from flask_injector import inject

from src.api.fields.users_fields_dto import resource_users_fields
from src.api.services.user_services import UserServices

from src.api.fields.users_fields_dto import resource_users_fields
from src.api.services.user_services import UserServices
from src.api.models.users import User


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("last_name", type=str, required=False, help="Last name can be entered")
    parser.add_argument("first_name", type=str, required=False, help="First name can be entered")
    parser.add_argument("email", type=str, required=True, help="Email for user cannot be blank")
    parser.add_argument("password", type=str, required=True, help="password for user cannot be blank")

    @inject
    def __init__(self, service: UserServices):
        self.user_services = service

    @jwt_required()
    @marshal_with(resource_users_fields)
    def get(self, uid=None):
        """
        Access informations on user
        ---
        tags:
          - users
        definitions:
          - schema:
              id: User
              properties:
                name:
                 type: string
                 description: the user's object
        parameters:
          - schema:
              id: User
              properties:
                last_name:
                  type: string
                  description: last name for user
                first_name:
                  type: string
                  description: firstname for user
                email:
                  type: string
                  description: email for user
                password:
                  type: string
                  description: password for user
        responses:
          201:
            description: return user
          401:
            description: return error
        """
        current_identity = get_jwt()

        if current_identity["role"] == "admin":
            pass
        elif get_jwt_identity() == uid or current_identity["role"] == "admin":
            # return {"id": get_jwt_identity(), "role": current_identity["role"]}
            return self.user_services.repository.find_by_id(User, uid)
        else:
            return {"error": "You cannot request this!"}, 401

    # @jwt_required()
    @marshal_with(resource_users_fields)
    def post(self):
        """
        Create a new user
        ---
        tags:
          - users
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
                last_name:
                  type: string
                  description: last name for user
                first_name:
                  type: string
                  description: firstname for user
                email:
                  type: string
                  description: email for user
                password:
                  type: string
                  description: password for user
        responses:
          201:
            description: User created
        """
        data = UserResource.parser.parse_args()
        return self.user_services.save_user(data["last_name"], data["first_name"], data["email"], data["password"])

    # @jwt_required()
    def delete(self, uid):
        pass

    # @jwt_required()
    def put(self, uid):
        pass
