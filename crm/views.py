from crm import app
from flask import render_template
from .models import Customer, Product, Order


@app.route('/', methods=['GET'])
def index():
    customers = Customer.query.all()
    orders = Order.query.all()

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
