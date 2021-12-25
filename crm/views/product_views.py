"""
This module contains views related to the products blueprint
"""
from flask import jsonify

from crm import db, app
from crm.models import Product
from crm.forms.product_form import ProductForm
from views.base_view import BaseListView, BaseDetailView


class ProductListView(BaseListView):

    def __init__(self):
        super().__init__()
        self.model = Product
        self.template_name = 'product/products.html'
        self.context = self.get_context

    def get_context(self):
        products = self.select_all()
        return {'products': products, 'total_products': len(products)}


class ProductCreateView(BaseListView):

    def __init__(self):
        super().__init__()
        self.model = Product
        self.template_name = 'product/product_create.html'
        self.context = self.get_context

    @staticmethod
    def get_context():
        return {'form': ProductForm()}


class ProductDetailView(BaseDetailView):

    def __init__(self):
        super().__init__()
        self.model = Product
        self.template_name = 'product/product_detail.html'
        self.context = self.get_context

    def get_context(self, id_):
        product = self.select_by_id(id_)
        self.model = product

        form = ProductForm(name=product, price=product.price, description=product.description)
        return {'product': product, 'form': form}
