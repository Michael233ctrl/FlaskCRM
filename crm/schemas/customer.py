from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from crm.models import Customer


class CustomerSchema(SQLAlchemyAutoSchema):
    """
    Customer serialization/deserialization schema
    """
    class Meta:
        model = Customer
