from flask_restful import fields


resource_exercices_fields = {
    "title": fields.String,
    "description": fields.String,
    "signature": fields.String,
    "url": fields.Url("exercises"),
}
