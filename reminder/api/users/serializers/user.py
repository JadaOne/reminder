from reminder.api.core.serializers import PublicBaseSchema
from rest_marshmallow import fields
from marshmallow import validate


class UserSchema(PublicBaseSchema):

    date_joined = fields.DateTime(dump_only=True)
    email = fields.Str(validate=validate.Email())
    first_name = fields.Str(validate=validate.Length(min=1, max=32))
    last_name = fields.Str(validate=validate.Length(min=1, max=32))
    password = fields.Str(load_only=True, validate=validate.Length(min=8))
