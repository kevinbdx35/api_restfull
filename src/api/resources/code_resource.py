from flask_injector import inject
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse, marshal_with

from src.api.fields.submitted_codes_fields_dto import resource_submitted_codes_fields
from src.api.services.code_services import CodeServices
from src.api.utils.constants import LOCALPATH

from src.api.fields.submitted_codes_fields_dto import resource_submitted_codes_fields
from src.api.services.code_services import CodeServices

import werkzeug


class CodeResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("files", type=werkzeug.datastructures.FileStorage, location="files",
                        help="You have to submit a code!!")

    @inject
    def __init__(self, service: CodeServices):
        self.service = service

    @jwt_required()
    @marshal_with(resource_submitted_codes_fields)
    def post(self, eid):
        """
        Submit a new code
        ---
        tags:
          - codes
        definitions:
          - schema:
              id: Code
              properties:
                name:
                 type: object
                 description: a code object
        parameters:
          - in: file
            name: files
            schema:
              id: Code
              required:
                - files
              properties:
                files:
                  type: path
                  description: solution of exercise from user
        responses:
          201:
            description: code created/submitted
          401:
            description: unauthorized user try to submit
        """
        data = CodeResource.parser.parse_args()
        current_user = get_jwt_identity()
        return self.service.repository.save_code(current_user, eid,
                                                 *self.service.save_file_locally(current_user, eid, data["files"]))

    # @jwt_required()
    def delete(self, cid):
        pass

    @jwt_required()
    @marshal_with(resource_submitted_codes_fields)
    def get(self, cid=None):
        pass

    # @jwt_required()
    def put(self, cid):
        pass
