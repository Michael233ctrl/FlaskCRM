from crm import app
from .models import Customer, Product, Order


@app.route('/')
def index():
    c = Customer.query.all()
    return f'Hello, {c}'



