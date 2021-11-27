from flask import Blueprint, render_template
from crm.models import Customer, Product, Order

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
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
