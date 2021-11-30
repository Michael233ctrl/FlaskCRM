from crm.rest import BaseListApi, BaseApi
from crm.schemas.order import OrderSchema
from crm.models import Order


class OrderListApi(BaseListApi):

    def __init__(self):
        super(OrderListApi, self).__init__()
        self.schema = OrderSchema()
        self.model = Order


class OrderApi(BaseApi):

    def __init__(self):
        super(OrderApi, self).__init__()
        self.schema = OrderSchema()
        self.model = Order
