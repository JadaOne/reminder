from .base import PublicBaseSchema
from rest_marshmallow import fields
from marshmallow import validate


class AddressSchema(PublicBaseSchema):
    address_1 = fields.Str(validate=validate.Length(min=0, max=100))
    address_2 = fields.Str(validate=validate.Length(min=0, max=100), required=False)

    postal_code = fields.Str(validate=validate.Length(min=0, max=20))
    city = fields.Str(validate=validate.Length(min=0, max=100))
    country = fields.Str(validate=validate.Length(min=0, max=100))
