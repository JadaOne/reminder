from uuid import UUID
from django.core.exceptions import ValidationError


def validate_UUID(value):

    try:
        UUID(value)
    except [ValueError, TypeError, AttributeError]:
        raise ValidationError
