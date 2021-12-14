"""
This module contains views related to the customers blueprint
"""
from flask import current_app as app
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request, abort

from crm import db
from crm.models import Customer
from crm.forms.customer_form import CustomerForm

customers = Blueprint('customers', __name__)


@customers.route('/customers', methods=['GET'])
def customer_list():
    """
    Render template with a list of all customers.

    :return: rendered `customers.html` template
    """
    customer = Customer.query.order_by('name').all()
    context = {
        'customers': customer,
        'total_customers': len(customer),
    }
    return render_template('customer/customers.html', **context)


@customers.route('/customers/<int:id>', methods=['GET', 'POST'])
def customer_detail(id):
    """
    On GET request render template with customer form and
    detailed information about customer. On POST request change
    information about customer.

    :param id: customer id
    :return: rendered `customer.html` template
    """
    customer = Customer.query.get(id)
    if not customer:
        app.logger.info(f"User entered wrong url")
        abort(404)

    form = CustomerForm(
        name=customer.name,
        surname=customer.surname,
        email=customer.email,
        phone=customer.phone
    )
    if request.method == 'POST':
        if form.validate_on_submit():
            customer.name = form.name.data
            customer.surname = form.surname.data
            customer.email = form.email.data
            customer.phone = form.phone.data
            db.session.commit()
            flash('User data was successfully updated', 'success')
            return redirect(url_for('customers.customer_detail', id=id))
        else:
            flash('Wrong entered data', 'danger')
    context = {
        'customer': customer,
        'form': form
    }
    return render_template('customer/customer_detail.html', **context)


@customers.route('/delete-customer/<id>', methods=['DELETE'])
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


@customers.route('/create-customer', methods=['GET', 'POST'])
def create_customer():
    """
    On GET request render template with customer creation form.
    On POST request add new customer.

    :return: rendered `customer_create.html` template
    """
    form = CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            customer = Customer(
                name=form.name.data,
                surname=form.surname.data,
                email=form.email.data,
                phone=form.phone.data
            )
            db.session.add(customer)
            db.session.commit()
            flash('Customer was successfully created', 'success')
            return redirect(url_for('customers.customer_list'))
        else:
            flash('Wrong entered data', 'danger')
    return render_template('customer/customer_create.html', form=form)
