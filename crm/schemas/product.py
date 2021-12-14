from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from crm.models import Product


class ProductSchema(SQLAlchemyAutoSchema):
    """
    Product serialization/deserialization schema
    """
    class Meta:
        model = Product
