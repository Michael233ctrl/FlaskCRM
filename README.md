# Flask CRM
[![Coverage Status](https://coveralls.io/repos/github/Michael233ctrl/FlaskCRM/badge.svg?branch=rebuild)](https://coveralls.io/github/Michael233ctrl/FlaskCRM?branch=rebuild)
___
## Description


#### “Flask CRM” is a web application that allows users to record information about clients, products, and orders.

The current version provides you functionality like:

- Storing customers, products, and orders in a database;
- Display the list of customers, products, and orders;
- Updating the list of customers, products, and orders (adding, editing, removing);
- Display number of customers, products, and orders;
- Display information about a specific customer, product, and order;
- Search customers and products.

## Installation

#### Clone repository:
```
git clone https://github.com/Michael233ctrl/FlaskCRM.git
```
#### Move to cloned folder:
````
cd FlaskCRM/
````


## How to run

#### Set up and activate the virtual environment:
````
python3 -m venv env
source env/bin/activate
````

#### Install the requirements:
```
pip install -r requirements.txt
```

#### Specify environment variables:
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
python -m crm.database.populate
```

#### Run the project locally:
```
python -m flask run
```
