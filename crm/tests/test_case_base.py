import unittest

from crm import models
from crm import app
from crm.models import Customer, Product, Order


class TestCaseBase(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        self.client = app.test_client()
        models.db.create_all()
        self.create_test_customer()
        self.create_test_product()
        self.create_test_order()

    def tearDown(self) -> None:
        models.db.session.remove()
        models.db.drop_all()

    def create_test_customer(self):
        customer_1 = Customer(name='John', surname='Doe', email='john@email.com', phone='434-555-198')
        customer_2 = Customer(name='Peter', surname='Piper', email='peter@email.com', phone='123-868-108')
        models.db.session.add(customer_1)
        models.db.session.add(customer_2)
        models.db.session.commit()

    def create_test_product(self):
        product_1 = Product(name='Airpods Wireless Bluetooth Headphones', price=119.99,
                            description='Bluetooth technology lets you connect it with '
                                        'compatible devices wirelesses High-quality AAC audio offers immersive list')
        product_2 = Product(name='Cannon EOS 80D DSLR Camera', price=929.99,
                            description='Characterized by versatile imaging specs, the Canon EOS 80D further clarifies'
                                        ' itself using a pair of robust focusing systems and an intuitive design')
        models.db.session.add(product_1)
        models.db.session.add(product_2)
        models.db.session.commit()

    def create_test_order(self):
        order_1 = Order(customer_id=Customer.query.get(1).id, product_id=Product.query.get(1).id)
        order_2 = Order(customer_id=Customer.query.get(2).id, product_id=Product.query.get(2).id)

        models.db.session.add(order_1)
        models.db.session.add(order_2)
        models.db.session.commit()
