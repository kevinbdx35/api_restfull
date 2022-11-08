from flask_restful import fields


resource_submitted_codes_fields = {
    "uid": fields.Integer,
    "eid": fields.Integer,
    "covrage": fields.Float,
    "time_stamp": fields.DateTime(dt_format='rfc822'),
    # "url": fields.Url("exercises/<>/code/"),
}
