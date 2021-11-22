from crm import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify
from .models import Customer, Product, Order
from .forms import CustomerForm


@app.route('/', methods=['GET'])
def dashboard():
    customers = Customer.query.all()[:5]
    products = Product.query.all()[:5]
    orders = Order.query.all()[:5]
    total_customers = Customer.query.count()
    total_orders = Order.query.count()
    total_products = Product.query.count()

    context = {
        'customers': customers,
        'orders': orders,
        'products': products,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'total_products': total_products,
    }

    return render_template('dashboard.html', **context)


@app.route('/customers', methods=['GET'])
def customer_list():
    customers = Customer.query.order_by('name').all()
    context = {
        'customers': customers,
        'total_customers': len(customers),
    }
    return render_template('customers.html', **context)


@app.route('/customer/<int:id>', methods=['GET', 'POST'])
def customer_detail(id):
    customer = Customer.query.get(id)
    form = CustomerForm()
    if form.validate_on_submit():
        customer.name = form.name.data
        customer.surname = form.surname.data
        customer.email = form.email.data
        customer.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('customer_detail', id=id))

    context = {
        'customer': customer,
        'form': form
    }
    return render_template('customer_detail.html', **context)


@app.route('/delete-customer/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(int(id))
    db.session.delete(customer)
    db.session.commit()
    return jsonify('Customer was deleted')


@app.route('/create-customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            phone=form.phone.data
        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('customer_list'))
    return render_template('customer_create.html', form=form)
