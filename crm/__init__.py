"""
Root module that initializes web application according to the flask factory pattern
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from crm.config import Config

MIGRATION_DIR = os.path.join('crm', 'migrations')

app = Flask(__name__)
app.config['SECRET_KEY'] = '0994e426533435a7a1c8c13de3414af4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/crm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

from crm.views import homepage_view, product_views, order_views

from crm.views.customer_views import CustomerListView, CustomerDetailView, CustomerCreateView
from crm.views.product_views import ProductListView, ProductDetailView, ProductCreateView

app.add_url_rule('/customers', view_func=CustomerListView.as_view('customer_list'))
app.add_url_rule('/customers/<id>', view_func=CustomerDetailView.as_view('customer_detail'))
app.add_url_rule('/create-customer', view_func=CustomerCreateView.as_view('create_customer'))

app.add_url_rule('/products', view_func=ProductListView.as_view('product_list'))
app.add_url_rule('/products/<id>', view_func=ProductDetailView.as_view('product_detail'))
app.add_url_rule('/create-product', view_func=ProductCreateView.as_view('create_product'))


# api = Api(app)


# from crm.rest.customer_api import CustomerListApi, CustomerApi
# from crm.rest.product_api import ProductListApi, ProductApi
# from crm.rest.order_api import OrderListApi, OrderApi
#
# api.add_resource(CustomerListApi, '/api/customers', strict_slashes=False)
# api.add_resource(CustomerApi, '/api/customers/<int:id>', strict_slashes=False)
#
# api.add_resource(ProductListApi, '/api/products', strict_slashes=False)
# api.add_resource(ProductApi, '/api/products/<int:id>', strict_slashes=False)
#
# api.add_resource(OrderListApi, '/api/orders', strict_slashes=False)
# api.add_resource(OrderApi, '/api/orders/<int:id>', strict_slashes=False)
