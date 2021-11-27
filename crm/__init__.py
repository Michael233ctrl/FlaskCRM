import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from psycopg2 import DatabaseError

MIGRATION_DIR = os.path.join('crm', 'migrations')

app = Flask(__name__)
app.config['SECRET_KEY'] = '0994e426533435a7a1c8c13de3414af4'
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/crm'
except DatabaseError as e:
    print('Connection failed')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

from crm.views import homepage_view, customer_views, product_views, order_views
