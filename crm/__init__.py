from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import DatabaseError

app = Flask(__name__)
app.config['SECRET_KEY'] = '0994e426533435a7a1c8c13de3414af4'
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/crm'
except DatabaseError as e:
    print('Connection failed')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from crm.views import homepage_view, customer_views, product_views, order_views
