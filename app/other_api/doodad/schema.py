from marshmallow import fields, Schema


class DoodadSchema(Schema):
    """Doodad schema"""

    doodadId = fields.Number(attribute="doodad_id")
    name = fields.String(attribute="name")
    purpose = fields.String(attribute="purpose")
