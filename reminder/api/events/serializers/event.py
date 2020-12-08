from rest_marshmallow import fields
from reminder.api.core.serializers import PublicBaseSchema
from marshmallow import validate
from .validators import FutureDateValidator
from .partisipant import PartisipantSchems


class EventSchema(PublicBaseSchema):

    title = fields.Str(validate=validate.Length(max=40), required=True)
    description = fields.Str(validate=validate.Length(max=1000))
    place = fields.Str(validate=validate.Length(max=128))
    date = fields.DateTime(validate=FutureDateValidator(), required=True)
    status = fields.Str(validate=validate.Length(max=32), dump_only=True)
    participants = fields.Method("get_participants")

    def get_participants(self, obj):
        return PartisipantSchems(obj.participants.all(), many=True).data
