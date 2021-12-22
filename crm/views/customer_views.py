"""
This module contains views related to the customers blueprint
"""
# from flask import current_app as app
from flask.views import MethodView

from crm import app, db

from flask import jsonify, render_template, flash, redirect, request

from crm.models import Customer
from crm.forms.customer_form import CustomerForm
# from views.base_view import BaseListView, BaseDetailView

from crm.service.view_service import select_all, select_by_id, create, update


class CustomerListView(MethodView):

    def __init__(self):
        self.template_name = 'customer/customers.html'
        self.context = {
            'customers': select_all(Customer),
            'total_customers': len(select_all(Customer))
        }

    def get(self):
        return render_template(self.template_name, **self.context)


class CustomerCreateView(MethodView):

    def __init__(self):
        super().__init__()
        self.model = Customer
        self.template_name = 'customer/customer_create.html'
        self.context = CustomerForm()

    def get(self):
        return render_template(self.template_name, form=self.context)

    def post(self):
        form = self.context
        if form.validate_on_submit():
            create(self.model, form.data)
            flash('Customer successfully created', 'success')
            return redirect(request.path)
        else:
            flash('Wrong entered data', 'danger')


class CustomerDetailView(MethodView):

    def __init__(self):
        super().__init__()
        self.model = Customer
        self.template_name = 'customer/customer_detail.html'

    def get(self, id):
        return render_template(self.template_name, **self.get_context(id))

    def get_context(self, id_):
        customer = select_by_id(self.model, id_)
        form = CustomerForm(
            name=customer.name,
            surname=customer.surname,
            email=customer.email,
            phone=customer.phone
        )
        return {'customer': customer, 'form': form}

    def post(self, id):
        data = self.get_context(id)
        item = data.get('customer') or data.get('product')

        form = data['form']
        if form.validate_on_submit():
            update(item, form.data)
            flash(f'{item} successfully updated', 'success')
            return redirect(request.path)
        else:
            flash('Wrong entered data', 'danger')


@app.route('/delete-customer/<id>', methods=['DELETE'])
def delete_customer(id):
    """
    Performs a delete request.

    :param id: customer id
    :return: json response
    """
    customer = Customer.query.get(int(id))
    db.session.delete(customer)
    db.session.commit()
    return jsonify('Customer was deleted')
