import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from psycopg2 import DatabaseError
from flask_restful import Api

MIGRATION_DIR = os.path.join('crm', 'migrations')

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = '0994e426533435a7a1c8c13de3414af4'
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/crm'
except DatabaseError as e:
    print('Connection failed')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

file_handler = logging.FileHandler(filename='app.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

app.logger.addHandler(file_handler)

from crm.views.homepage_view import home
from crm.views.customer_views import customers
from crm.views.product_views import products
from crm.views.order_views import orders
from crm.views.handling_error_views import bp

app.register_blueprint(home)
app.register_blueprint(customers)
app.register_blueprint(products)
app.register_blueprint(orders)
app.register_blueprint(bp)

from crm.rest.customer_api import CustomerListApi, CustomerApi
from crm.rest.product_api import ProductListApi, ProductApi
from crm.rest.order_api import OrderListApi, OrderApi

api.add_resource(CustomerListApi, '/api/customers', strict_slashes=False)
api.add_resource(CustomerApi, '/api/customers/<int:id>', strict_slashes=False)

api.add_resource(ProductListApi, '/api/products', strict_slashes=False)
api.add_resource(ProductApi, '/api/products/<int:id>', strict_slashes=False)

api.add_resource(OrderListApi, '/api/orders', strict_slashes=False)
api.add_resource(OrderApi, '/api/orders/<int:id>', strict_slashes=False)


def create_app():
    pass
