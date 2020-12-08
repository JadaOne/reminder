from rest_marshmallow import Schema, fields


class AbstractBaseSchema(Schema):

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class PublicBaseSchema(AbstractBaseSchema):

    pub_id = fields.UUID(dump_only=True)
