from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask_injector import inject
from src.api.services.admin_services import AdminServices


class AdminResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Email for user cannot be blank")
    parser.add_argument("password", type=str, required=True, help="password for user cannot be blank")

    @inject
    def __init__(self, service: AdminServices):
        self.admin_services = service

    @jwt_required()
    def post(self):
        pass
        # data = AdminResource.parser.parse_args()
        # return self.admin_services.save_admin(data["email"], data["password"])

    # @jwt_required()
    def delete(self, aid):
        pass

    # @jwt_required()
    def get(self, aid=None):
        pass

    # @jwt_required()
    def put(self, aid):
        pass
