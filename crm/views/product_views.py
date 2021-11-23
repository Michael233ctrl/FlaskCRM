from crm import app, db
from flask import render_template
from crm.models import Product


@app.route('/products', methods=['GET'])
def product_list():
    products = Product.query.order_by('name').all()
    context = {
        'products': products,
        'total_products': len(products),
    }
    return render_template('products.html', **context)


