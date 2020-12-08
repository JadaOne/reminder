from marshmallow import validate
from rest_marshmallow import fields

from reminder.api.core.serializers import PublicBaseSchema

from .partisipant import ParticipantSchema
from .validators import FutureDateValidator


class EventSchema(PublicBaseSchema):

    title = fields.Str(validate=validate.Length(max=40), required=True)
    description = fields.Str(validate=validate.Length(max=1000))
    place = fields.Str(validate=validate.Length(max=128))
    date = fields.DateTime(validate=FutureDateValidator(), required=True)
    status = fields.Str(validate=validate.Length(max=32), dump_only=True)
    participants = fields.Method("get_participants")

    def get_participants(self, obj):
        return ParticipantSchema(obj.participants.all(), many=True).data
