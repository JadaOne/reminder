from django.utils.timezone import now
from marshmallow import ValidationError
from marshmallow.validate import Validator


class FutureDateValidator(Validator):
    def __call__(self, value):

        now_ = now()
        value = value.replace(tzinfo=now_.tzinfo)
        if value <= now_:
            raise ValidationError("Event can not take place in the past.")
        return value
