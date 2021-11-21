from datetime import datetime
from crm import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    order = db.relationship('Order', backref='customer', lazy=True)

    def __repr__(self):
        return f'{self.name} {self.surname}'

    @property
    def orders(self):
        order_count = len(self.order)
        return str(order_count)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    order = db.relationship('Order', backref='product', lazy=True)

    def __repr__(self):
        return self.name


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return str(self.product_id)
