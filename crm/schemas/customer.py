from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from crm.models import Customer


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
