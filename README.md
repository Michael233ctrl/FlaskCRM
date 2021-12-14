# Flask CRM
[![Coverage Status](https://coveralls.io/repos/github/Michael233ctrl/FlaskCRM/badge.svg?branch=rebuild)](https://coveralls.io/github/Michael233ctrl/FlaskCRM?branch=rebuild)
___
##Description
####Flask CRM is a simple web application that allows you to manage your company and interact with customers.

The current version provides you functionality like:
- display a list of all customers, products, and orders.
- display particular customer or product.
- search customers and products.
- update, create and delete customers, products, and orders.

##Installation

####Clone repository:
```
git clone https://github.com/Michael233ctrl/FlaskCRM.git
```
####Move to cloned folder:
````
cd FlaskCRM/
````


## How to run

####Set up and activate the virtual environment:
````
python3 -m venv env
source env/bin/activate
````

#### Install the requirements:
```
pip install -r requirements.txt
```

####Specify environment variables:
````
SECRET_KEY=<your_secret_key>
SQLALCHEMY_DATABASE_URI=<your_postgres_server>
FLASK_APP=run.py
````

#### Run migrations to create database infrastructure:
```
flask db upgrade
```

#### Populate the database with data (optionally)
```
python -m crm/database/populate.py
```

#### Run the project locally:
```
python -m flask run
```
