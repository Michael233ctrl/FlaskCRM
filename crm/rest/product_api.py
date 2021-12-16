"""
This module defines the following classes:
 - ProductListApi, product list API class
 - ProductApi, product API class
"""
from crm.rest.base_api import BaseListApi, BaseApi
from crm.schemas.product import ProductSchema
from crm.models import Product


class ProductListApi(BaseListApi):
    """
    Product list API class
    """

    def __init__(self):
        super(ProductListApi, self).__init__()

        #: Marshmallow schema used for product serialization/deserialization
        self.schema = ProductSchema()

        #: Product model
        self.model = Product


class ProductApi(BaseApi):
    """
    Product API class
    """

    def __init__(self):
        super(ProductApi, self).__init__()

        #: Marshmallow schema used for product serialization/deserialization
        self.schema = ProductSchema()

        #: Product model
        self.model = Product
