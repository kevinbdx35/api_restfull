from flask_restful import fields


resource_users_fields = {
    "uid": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "url": fields.Url("users"),
}
