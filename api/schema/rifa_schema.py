from . import fields, SQLAlchemySchema



class RifaSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):

        fields = (
            "id",
            "nombre",
            "imagen"
        )

    id = fields.Integer()
    nombre = fields.String()
    imagen = fields.String()

    