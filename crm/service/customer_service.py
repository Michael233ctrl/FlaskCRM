from crm import db
from crm.models import Customer


def select_all():
    return db.session.query(Customer).all()


def select_by_id(customer_id):
    return db.session.query(Customer).get(customer_id)


def create_customer(**kwargs):
    customer = Customer(**kwargs)
    db.session.add(customer)
    db.session.commit()
    return customer


def update_customer(customer_id, **kwargs):
    customer = select_by_id(customer_id)
    if customer:
        customer.update(**kwargs)
        db.session.commit()
        return customer
    return False


def delete_customer(customer_id):
    customer = select_by_id(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return customer
    return False
