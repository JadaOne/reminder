from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _lazy
import re


EMAIL_REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def validate_email(value):
    if not re.search(EMAIL_REGEX, value):
        raise ValidationError(_lazy('Invalid Email'))
    return value
