from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from crm.models import Order


class OrderSchema(SQLAlchemyAutoSchema):
    """
    Order serialization/deserialization schema
    """
    class Meta:
        model = Order
        include_fk = True
