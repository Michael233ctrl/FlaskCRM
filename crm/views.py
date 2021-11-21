from crm import app
from flask import render_template
from .models import Customer, Product, Order


@app.route('/', methods=['GET'])
def dashboard():
    customers = Customer.query.all()[:5]
    orders = Order.query.all()[:5]
    total_customers = Customer.query.count()
    total_orders = Order.query.count()
    total_products = Product.query.count()

    context = {
        'customers': customers,
        'orders': orders,
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


@app.route('/customer/<int:id>')
def customer_detail(id):
    customer = Customer.query.get(id)
    return render_template('customer_detail.html', customer=customer)


