from crm.rest.base_api import BaseListApi, BaseApi
from crm.schemas.customer import CustomerSchema
from crm.models import Customer


class CustomerListApi(BaseListApi):

    def __init__(self):
        super(CustomerListApi, self).__init__()
        self.schema = CustomerSchema()
        self.model = Customer


class CustomerApi(BaseApi):

    def __init__(self):
        super(CustomerApi, self).__init__()
        self.schema = CustomerSchema()
        self.model = Customer
