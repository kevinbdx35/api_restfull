from flask import Flask, jsonify
from flask_injector import FlaskInjector, request
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_swagger import swagger

from src.api.repositories.generic_repository import GenericRepository
from src.api.repositories.user_repository import UserRepository
from src.api.repositories.exercice_repository import ExerciceRepository

from src.api.resources.login_resource import LoginAdmin, LoginUser
from src.api.resources.admin_resource import AdminResource
from src.api.resources.code_resource import CodeResource
from src.api.resources.exercise_resource import ExerciseResource
from src.api.resources.user_resource import UserResource

from src.api.services.admin_services import AdminServices
from src.api.services.user_services import UserServices
from src.api.services.code_services import CodeServices
from src.api.services.exercise_services import ExerciseServices

from src.api.utils.cryptography import bcrypt

import json
import os


def __configure_api(mode):
    """
    Parse configuration parameters from json conf file to return url to database and secret key fro JWT

    :param mode: change environment to mode
    :return: url_2_postgres_database, jwt_key
    """
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'configgame.json')), "r") as j:
        data = json.load(j)

    return (f"postgresql://{data[mode]['user']}:{data[mode]['password']}@{data[mode]['host']}/{data[mode]['db']}",
            data[mode]["jwt_key"])


def create_app(mode):
    """
    Create the application

    :param mode: change environment to mode
    :return: app (Flask obect)
    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"], app.config["JWT_SECRET_KEY"] = __configure_api(mode)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 60*60*24*7  # token expired after one week

    bcrypt.init_app(app)
    jwt = JWTManager(app)
    api = Api(app)

    @app.before_first_request
    def __initialize_db():
        """
        Initialize database before the first request for further use
        :return: None
        """
        from src.api.utils.database import db
        db.init_app(app)
        db.create_all()

    # ressources exerices, user, login, admin
    api.add_resource(AdminResource, "/admins", endpoint="admins")
    api.add_resource(ExerciseResource, "/exercises", "/exercises/<int:eid>", endpoint="exercises")
    api.add_resource(CodeResource, "/exercises/<int:eid>/submit", endpoint="exercises/<>/submit")
    api.add_resource(UserResource, "/users", "/users/<int:uid>",  endpoint="users")
    api.add_resource(LoginAdmin, "/admins/login",  endpoint="/admins/login")
    api.add_resource(LoginUser, "/users/login",  endpoint="/users/login")

    def inject_configuration(binder):
        binder.bind(AdminServices, to=AdminServices, scope=request)
        binder.bind(UserServices, to=UserServices, scope=request)
        binder.bind(CodeServices, to=CodeServices, scope=request)
        binder.bind(ExerciseServices, to=ExerciseServices, scope=request)
        # binder.bind(UserRepository, to=UserRepository, scope=request)
        # binder.bind(GenericRepository, to=GenericRepository, scope=request)
        # binder.bind(ExerciceRepository, to=ExerciceRepository, scope=request)

    FlaskInjector(app=app, modules=[inject_configuration])

    @app.route("/docs")
    def docs():
        return jsonify(swagger(app))

    return app
