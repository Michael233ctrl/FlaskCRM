"""
This module contains views related to the orders blueprint
"""

from flask import flash, redirect, url_for

from crm import db, app
from crm.models import Order, Customer, Product
from crm.forms.order_form import OrderForm
from views.base_view import BaseListView, BaseDetailView


class OrderListView(BaseListView):

    def __init__(self):
        super().__init__()
        self.model = Order
        self.template_name = 'order/orders.html'
        self.context = self.get_context

    def get_context(self):
        orders = self.select_all()
        return {'orders': orders, 'total_orders': len(orders)}


class OrderCreateView(BaseListView):

    def __init__(self):
        super().__init__()
        self.model = Order
        self.template_name = 'order/order_form.html'
        self.context = self.get_context

    def get_context(self):
        form = OrderForm()
        form.customer.choices = [(c.id, c) for c in self.select_all(Customer)]
        form.product.choices = [(p.id, p) for p in self.select_all(Product)]
        return {'form': form}

    def post(self):
        data = self.context()
        form = data.get('form')

        if form.validate_on_submit():
            order = Order(
                customer_id=form.customer.data,
                product_id=form.product.data,
            )
            self.save(order)
            flash('Order was successfully created', 'success')
            return redirect(url_for('order_list'))
        else:
            flash('Wrong entered data', 'danger')


class OrderUpdateView(BaseDetailView):

    def __init__(self):
        super().__init__()
        self.model = Order
        self.template_name = 'order/order_form.html'
        self.context = self.get_context

    def get_context(self, id_):
        order = self.select_by_id(id_)
        self.model = order

        form = OrderForm(customer=order.customer_id, product=order.product_id)
        form.customer.choices = [(c.id, c) for c in self.select_all(Customer)]
        form.product.choices = [(p.id, p) for p in self.select_all(Product)]
        return {'form': form, 'order': order}

    def post(self, id):
        data = self.context(id)
        form = data.get('form')
        order = data.get('order')

        if form.validate_on_submit():
            order.customer_id = form.customer.data
            order.product_id = form.product.data

            self.save()
            flash('Order was successfully updated', 'success')
            return redirect(url_for('order_list'))
        else:
            flash('Wrong entered data', 'danger')


# class OrderDeleteView(ServiceDB, MethodView):
#
#     def __init__(self):
#         super().__init__()
#         self.model = Order
#     #     self.context = self.get_context
#     #
#     # def get_context(self, id_):
#     #     order = self.select_by_id(id_)
#     #     return order
#
#     def get(self, id):
#         self.delete_item(id)
#         flash(f'Order:{id} was successfully deleted', 'success')
#         return redirect(url_for('order_list'))


@app.route('/delete-order/<int:id>')
def delete_order(id):
    """
    Performs a delete request.

    :param id: order id
    :return: redirects to order_list
    """
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    flash('Order was successfully deleted', 'success')
    return redirect(url_for('order_list'))
