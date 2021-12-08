from crm.rest.base_api import BaseListApi, BaseApi
from crm.schemas.product import ProductSchema
from crm.models import Product


class ProductListApi(BaseListApi):

    def __init__(self):
        super(ProductListApi, self).__init__()
        self.schema = ProductSchema()
        self.model = Product


class ProductApi(BaseApi):

    def __init__(self):
        super(ProductApi, self).__init__()
        self.schema = ProductSchema()
        self.model = Product



