from crm import app, db
from flask import render_template, flash, redirect, url_for, jsonify
from crm.models import Product
from crm.forms.product_form import ProductForm


@app.route('/products', methods=['GET'])
def product_list():
    products = Product.query.order_by('name').all()
    context = {
        'products': products,
        'total_products': len(products),
    }
    return render_template('products.html', **context)


@app.route('/product/<int:id>', methods=['GET', 'POST'])
def product_detail(id):
    product = Product.query.get(id)
    form = ProductForm()
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.description = form.description.data
        db.session.commit()
        flash('Product data was successfully updated', 'success')
        return redirect(url_for('product_detail', id=id))
    context = {
        'product': product,
        'form': form
    }
    return render_template('product_detail.html', **context)


@app.route('/delete-product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(int(id))
    db.session.delete(product)
    db.session.commit()
    return jsonify('Customer was deleted')