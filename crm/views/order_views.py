from crm import app, db
from flask import render_template, flash, redirect, url_for, request
from crm.models import Order
from crm.forms.order_form import OrderForm


@app.route('/orders', methods=['GET'])
def order_list():
    orders = Order.query.all()
    context = {
        'orders': orders,
        'total_orders': len(orders),
    }
    return render_template('orders.html', **context)


@app.route('/update-order/<int:id>', methods=['GET', 'POST'])
def update_order(id):
    order = Order.query.get(id)
    form = OrderForm(customer=order.customer_id, product=order.product_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            order.customer_id = form.customer.data
            order.product_id = form.product.data
            db.session.commit()
            flash('Order was successfully updated', 'success')
            return redirect(url_for('order_list'))
        else:
            flash('Wrong entered data', 'danger')
    context = {
        'action': 'update',
        'form': form
    }
    return render_template('order_form.html', **context)


@app.route('/delete-order/<int:id>')
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    flash('Order was successfully deleted', 'success')
    return redirect(url_for('order_list'))


@app.route('/create-order/', methods=['GET', 'POST'])
def create_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = Order(
            customer_id=form.customer.data,
            product_id=form.product.data,
        )
        db.session.add(order)
        db.session.commit()
        flash('Order was successfully created', 'success')
        return redirect(url_for('order_list'))
    return render_template('order_form.html', form=form)
