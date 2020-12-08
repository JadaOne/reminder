from rest_marshmallow import fields, Schema
from marshmallow import validate
from reminder.api.users.serializers import UserSchema


class CreateParticipantSchema(Schema):

    emails = fields.List(fields.Email(), required=True)


class PartisipantSchems(Schema):

    user = fields.Nested(UserSchema)
    role = fields.Str(validate=validate.Length(max=32))
