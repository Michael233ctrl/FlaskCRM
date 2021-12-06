from crm import db
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request, abort
from crm.models import Customer
from crm.forms.customer_form import CustomerForm

customers = Blueprint('customers', __name__)


@customers.route('/customers', methods=['GET'])
def customer_list():
    customer = Customer.query.order_by('name').all()
    context = {
        'customers': customer,
        'total_customers': len(customer),
    }
    return render_template('customer/customers.html', **context)


@customers.route('/customers/<int:id>', methods=['GET', 'POST'])
def customer_detail(id):
    customer = Customer.query.get(id)
    if not customer:
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
    customer = Customer.query.get(int(id))
    db.session.delete(customer)
    db.session.commit()
    return jsonify('Customer was deleted')


@customers.route('/create-customer', methods=['GET', 'POST'])
def create_customer():
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
