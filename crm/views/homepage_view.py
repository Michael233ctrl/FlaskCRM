from flask import Blueprint, render_template, request
from crm.models import Customer, Product, Order

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def dashboard():
    customers = Customer.query.limit(5).all()
    products = Product.query.limit(5).all()
    orders = Order.query.limit(5).all()
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


@home.route('/search', methods=['GET'])
def search():
    searched = request.args.get('q')
    if searched:
        q_customer = Customer.query.filter(
            Customer.name.ilike(f'%{searched}%') | Customer.surname.ilike(f'%{searched}%')
        ).all()
        q_product = Product.query.filter(
            Product.name.ilike(f'%{searched}%') | Product.description.ilike(f'%{searched}%')
        ).all()
        return render_template('search.html', searched=searched, q_customer=q_customer, q_product=q_product)
    return render_template('search.html')
