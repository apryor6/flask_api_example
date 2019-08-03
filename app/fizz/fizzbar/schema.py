from marshmallow import fields, Schema


class FizzbarSchema(Schema):
    """Fizzbar schema"""

    fizzbarId = fields.Number(attribute="fizzbar_id")
    name = fields.String(attribute="name")
    purpose = fields.String(attribute="purpose")
