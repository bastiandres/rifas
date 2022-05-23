# from flask_marshmallow import Schema
# from marshmallow.fields import Integer, Str
from dataclasses import field
from . import fields, SQLAlchemySchema

class TicketSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        fields = [
            "id",
            "nombre",
            "sold_by",
            "id_rifa"
        ]

    id = fields.Integer()
    nombre = fields.Str()
    sold_by = fields.Str()
    id_rifa = fields.Integer()