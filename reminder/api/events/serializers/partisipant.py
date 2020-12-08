from marshmallow import validate
from rest_marshmallow import Schema, fields

from reminder.api.users.serializers import UserSchema


class CreateParticipantSchema(Schema):

    emails = fields.List(fields.Email(), required=True)


class ParticipantSchema(Schema):

    user = fields.Nested(UserSchema)
    role = fields.Str(validate=validate.Length(max=32))
