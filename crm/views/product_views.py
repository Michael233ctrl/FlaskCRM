"""
This module contains views related to the products blueprint
"""
from flask import jsonify

from crm import db, app
from crm.models import Product
from crm.forms.product_form import ProductForm
from views.base_view import BaseListView, BaseDetailView

from crm.service.view_service import select_all


class ProductListView(BaseListView):

    def __init__(self):
        super().__init__()
        self.template_name = 'product/products.html'
        self.model = Product
        self.context = self.get_context()

    def get_context(self):
        product = select_all(self.model)
        return {'products': product, 'total_products': len(product)}


class ProductCreateView(BaseListView):

    def __init__(self):
        super().__init__()
        self.model = Product
        self.template_name = 'product/product_create.html'
        self.context = {'form': ProductForm()}


class ProductDetailView(BaseDetailView):

    def __init__(self):
        super().__init__()
        self.template_name = 'product/product_detail.html'

    def get_context(self, id_):
        product = Product.query.get(id_)
        form = ProductForm(name=product, price=product.price, description=product.description)
        return {'product': product, 'form': form}




@app.route('/delete-product/<id>', methods=['DELETE'])
def delete_product(id):
    """
    Performs a delete request.

    :param id: product id
    :return: json response
    """
    product = Product.query.get(int(id))
    db.session.delete(product)
    db.session.commit()
    return jsonify('Product was deleted')

