from marshmallow import fields, Schema


class WidgetSchema(Schema):
    """Widget schema"""

    widgetId = fields.Number(attribute="widget_id")
    name = fields.String(attribute="name")
    purpose = fields.String(attribute="purpose")
