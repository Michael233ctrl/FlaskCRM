"""
This module contains database models and defines the following classes:
 - Customer
 - Product
 - Order
"""
from datetime import datetime
from crm import db


class Customer(db.Model):
    """
    This class defines a database table for customer

    :param (str) name: customer name
    :param (str) surname: customer surname
    :param (str) email: customer email
    :param (str) phone: customer phone
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    order = db.relationship('Order', backref='customer', cascade="all,delete", lazy=True)

    def __init__(self, name, surname, email, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f'{self.name} {self.surname}'

    @property
    def orders(self):
        order_count = len(self.order)
        return str(order_count)


class Product(db.Model):
    """
    This class defines a database table for product

    :param (str) name: customer name
    :param (float) price: customer surname
    :param (str) description: customer email
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    order = db.relationship('Order', backref='product', cascade="all,delete", lazy=True)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        return self.name


class Order(db.Model):
    """This class defines a database table for order"""
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return str(self.product_id)
