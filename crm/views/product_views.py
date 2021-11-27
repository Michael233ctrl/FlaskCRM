from crm import db
from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from crm.models import Product
from crm.forms.product_form import ProductForm


products = Blueprint('products', __name__)


@products.route('/products', methods=['GET'])
def product_list():
    product = Product.query.order_by('name').all()
    context = {
        'products': product,
        'total_products': len(product),
    }
    return render_template('product/products.html', **context)


@products.route('/product/<int:id>', methods=['GET', 'POST'])
def product_detail(id):
    product = Product.query.get(id)
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
    product = Product.query.get(int(id))
    db.session.delete(product)
    db.session.commit()
    return jsonify('Product was deleted')


@products.route('/create-product', methods=['GET', 'POST'])
def create_product():
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
