"""
Root module that initializes web application according to the flask factory pattern
"""
import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from crm.config import Config

MIGRATION_DIR = os.path.join('crm', 'migrations')

db = SQLAlchemy()
migrate = Migrate()


def create_app(testing: object = None):
    """
    An application factory. Function creates and configures the main flask instance.

    :param testing: can be used for testing application, default None
    :return: flask application
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    if testing:
        app.config.from_object(testing)

    api = Api(app)
    db.init_app(app)
    migrate.init_app(app, db, directory=MIGRATION_DIR)

    if not testing:
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

    return app
