from crm import app, db
from flask import render_template, flash, redirect, url_for, jsonify
from crm.models import Order, Customer, Product
from crm.forms.order_form import OrderForm


@app.route('/orders', methods=['GET'])
def order_list():
    orders = Order.query.all()
    context = {
        'orders': orders,
        'total_orders': len(orders),
    }
    return render_template('orders.html', **context)


@app.route('/orders/<int:id>', methods=['GET', 'POST'])
def update_order(id):
    order = Order.query.get(id)
    form = OrderForm(customer=order.customer_id, product=order.product_id)
    if form.validate_on_submit():
        order.customer_id = form.customer.data
        order.product_id = form.product.data
        db.session.commit()
        return redirect(url_for('order_list'))

    context = {
        'action': 'update',
        'form': form
    }
    return render_template('order_form.html', **context)
