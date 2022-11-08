from flask_restful import Resource, reqparse, marshal_with
from flask_injector import inject
from flask_jwt_extended import jwt_required
from src.api.fields.exercices_fields_dto import resource_exercices_fields
from src.api.services.exercise_services import ExerciseServices
from src.api.models.exercises import Exercise
from datetime import datetime


class ExerciseResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=False, help="Title for user cannot be blank")
    parser.add_argument("description", type=str, required=True, help="Description can be entered")
    parser.add_argument("signature", type=str, required=False, help="Signature cannot be blank")
    parser.add_argument("test_code", type=str, required=False, help="Code for test cannot be blank")

    @inject
    def __init__(self, service: ExerciseServices):
        self.service = service

    # @jwt_required()
    @marshal_with(resource_exercices_fields)
    def get(self, eid=None):
        """
        Access exercises
        ---
        tags:
          - exercises
        definitions:
          - schema:
              id: Exercise
              properties:
                name:
                 type: object
                 description: Exercise object
        parameters:
          - in: none
            name: none
            schema:
              id: Exercise
              properties:
                title:
                  type: string
                  description: title of exercise
                description:
                  type: string
                  description: specification of exercise
                signature:
                  type: string
                  description: signature of exercise
                url:
                  type: string
                  description: url to exercise
        responses:
          201:
            description: list of exercise(s)
        """
        if eid is None:
            return self.service.repository.find_all(Exercise)
        else:
            return self.service.repository.find_by_id(Exercise, eid)

    @jwt_required()
    @marshal_with(resource_exercices_fields)
    def post(self):
        """
        Create en exercises
        ---
        tags:
          - exercises
        definitions:
          - schema:
              id: Exercise
              properties:
                name:
                 type: object
                 description: en exercise object
        parameters:
          - in: body
            name: body
            schema:
              id: Exercise
              required:
                - token
                - password
              properties:
                title:
                  type: string
                  description: title of exercise
                signature:
                  type: string
                  description: signature of exercise
                test_code:
                  type: string
                  description: code to test exercise
                description:
                  type: string
                  description: specification for user
        responses:
          201:
            description: exercise created
          401:
            description: unauthorized user (not admin)
        """
        data = ExerciseResource.parser.parse_args()
        return self.service.save_exercice(data["title"], data["signature"], data["test_code"], datetime.now(),
                                          data["description"] or None)

    # @jwt_required()
    def delete(self, eid):
        pass

    # @jwt_required()
    def put(self, eid):
        pass
