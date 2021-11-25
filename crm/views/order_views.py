from crm import app, db
from flask import render_template, flash, redirect, url_for, jsonify
from crm.models import Order
from crm.forms.product_form import ProductForm


@app.route('/orders', methods=['GET'])
def order_list():
    orders = Order.query.all()
    context = {
        'orders': orders,
        'total_orders': len(orders),
    }
    return render_template('orders.html', **context)