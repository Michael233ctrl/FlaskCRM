"""
This module contains views related to the products blueprint
"""
from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request, abort
from flask import current_app as app

from crm import db
from crm.models import Product
from crm.forms.product_form import ProductForm


products = Blueprint('products', __name__)


@products.route('/products', methods=['GET'])
def product_list():
    """
    Render template with a list of all products.

    :return: rendered `products.html` template
    """
    product = Product.query.order_by('name').all()
    context = {
        'products': product,
        'total_products': len(product),
    }
    return render_template('product/products.html', **context)


@products.route('/products/<int:id>', methods=['GET', 'POST'])
def product_detail(id):
    """
    On GET request render template with product form and
    detailed information about product. On POST request change
    information about product.

    :param id: product id
    :return: rendered `product_detail.html` template
    """
    product = Product.query.get(id)
    if not product:
        app.logger.info(f"User entered wrong url")
        abort(404)

    form = ProductForm(name=product, price=product.price, description=product.description)
    if request.method == 'POST':
        if form.validate_on_submit():
            product.name = form.name.data
            product.price = form.price.data
            product.description = form.description.data
            db.session.commit()
            flash('Product data was successfully updated', 'success')
            return redirect(url_for('products.product_detail', id=id))
        else:
            flash('Wrong entered data', 'danger')
    context = {
        'product': product,
        'form': form
    }
    return render_template('product/product_detail.html', **context)


@products.route('/delete-product/<id>', methods=['DELETE'])
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


@products.route('/create-product', methods=['GET', 'POST'])
def create_product():
    """
    On GET request render template with product creation form.
    On POST request add new product.

    :return: rendered `product_create.html` template
    """
    form = ProductForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            product = Product(
                name=form.name.data,
                price=form.price.data,
                description=form.description.data,
            )
            db.session.add(product)
            db.session.commit()
            flash('Product data was successfully created', 'success')
            return redirect(url_for('products.product_list'))
        else:
            flash('Wrong entered data', 'danger')
    return render_template('product/product_create.html', form=form)
