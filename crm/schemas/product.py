from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from crm.models import Product


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product