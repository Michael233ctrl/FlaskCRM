"""
This module defines the following classes:
 - OrderListApi, order list API class
 - OrderApi, order API class
"""
from crm.rest.base_api import BaseListApi, BaseApi
from crm.schemas.order import OrderSchema
from crm.models import Order


class OrderListApi(BaseListApi):
    """
    Order list API class
    """

    def __init__(self):
        super(OrderListApi, self).__init__()

        #: Marshmallow schema used for order serialization/deserialization
        self.schema = OrderSchema()

        #: Order model
        self.model = Order


class OrderApi(BaseApi):
    """
    Order API class
    """

    def __init__(self):
        super(OrderApi, self).__init__()

        #: Marshmallow schema used for order serialization/deserialization
        self.schema = OrderSchema()

        #: Order model
        self.model = Order
