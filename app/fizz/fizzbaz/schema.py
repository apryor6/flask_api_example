from marshmallow import fields, Schema


class FizzbazSchema(Schema):
    """Fizzbaz schema"""

    fizzbazId = fields.Number(attribute="fizzbaz_id")
    name = fields.String(attribute="name")
    purpose = fields.String(attribute="purpose")
