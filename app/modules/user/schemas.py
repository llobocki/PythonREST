from marshmallow import Schema, fields, post_load

from app.modules.user import models


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    surname = fields.String()
