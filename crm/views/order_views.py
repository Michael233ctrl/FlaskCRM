from crm import db
from flask import Blueprint, render_template, flash, redirect, url_for, request
from crm.models import Order, Customer, Product
from crm.forms.order_form import OrderForm

orders = Blueprint('orders', __name__)


@orders.route('/orders', methods=['GET'])
def order_list():
    order = Order.query.all()
    context = {
        'orders': order,
        'total_orders': len(order),
    }
    return render_template('order/orders.html', **context)


@orders.route('/update-order/<int:id>', methods=['GET', 'POST'])
def update_order(id):
    order = Order.query.get(id)
    form = OrderForm(customer=order.customer_id, product=order.product_id)
    form.customer.choices = [(c.id, c) for c in Customer.query.all()]
    form.product.choices = [(c.id, c) for c in Product.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            order.customer_id = form.customer.data
            order.product_id = form.product.data
            db.session.commit()
            flash('Order was successfully updated', 'success')
            return redirect(url_for('orders.order_list'))
        else:
            flash('Wrong entered data', 'danger')
    context = {
        'action': 'update',
        'form': form
    }
    return render_template('order/order_form.html', **context)


@orders.route('/delete-order/<int:id>')
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    flash('Order was successfully deleted', 'success')
    return redirect(url_for('orders.order_list'))


@orders.route('/create-order/', methods=['GET', 'POST'])
def create_order():
    form = OrderForm()
    form.customer.choices = [(c.id, c) for c in Customer.query.all()]
    form.product.choices = [(c.id, c) for c in Product.query.all()]
    if form.validate_on_submit():
        order = Order(
            customer_id=form.customer.data,
            product_id=form.product.data,
        )
        db.session.add(order)
        db.session.commit()
        flash('Order was successfully created', 'success')
        return redirect(url_for('orders.order_list'))
    return render_template('order/order_form.html', form=form)
