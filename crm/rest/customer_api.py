"""
This module defines the following classes:
 - CustomerListApi, customer list API class
 - CustomerApi, customer API class
"""
from crm.rest.base_api import BaseListApi, BaseApi
from crm.schemas.customer import CustomerSchema
from crm.models import Customer


class CustomerListApi(BaseListApi):
    """
    Customer list API class
    """

    def __init__(self):
        super(CustomerListApi, self).__init__()

        #: Marshmallow schema used for customer serialization/deserialization
        self.schema = CustomerSchema()

        #: Customer model
        self.model = Customer


class CustomerApi(BaseApi):
    """
    Customer API class
    """

    def __init__(self):
        super(CustomerApi, self).__init__()

        #: Marshmallow schema used for customer serialization/deserialization
        self.schema = CustomerSchema()

        #: Customer model
        self.model = Customer
