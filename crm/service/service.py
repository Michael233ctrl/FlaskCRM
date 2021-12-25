"""
This module used to make database queries
"""
from crm import db


def select_all(model):
    """
    Fetches all records from a database.

    :param model: database model
    :return: list of all by a given model
    """
    return db.session.query(model).all()


def select_by_id(model, id):
    """
    Fetches record by id from a database.

    :param model: database model
    :return: record with a given id
    """
    return db.session.query(model).get(id)


def create(model, data):
    """
    Create a new record in the database by a given model
    and with a given data.

    :param model: database model
    :param data: given data
    :return: created record
    """
    for k in data:
        if not hasattr(model, k):
            raise AttributeError
    item = model(**data)
    db.session.add(item)
    db.session.commit()
    return item


def update(model, id, data):
    """
    Update record in a given model by id.

    :param model: database model
    :param id: record id
    :param data: given data
    :return: record
    """
    item = select_by_id(model, id)
    if item:
        for key, value in data.items():
            if not hasattr(item, key):
                raise AttributeError
            setattr(item, key, value)
        db.session.commit()
        return item
    raise ValueError


def delete(model, id):
    """
    Delete record by a given id.

    :param model: database model
    :param id: record id
    :return: deleted record
    """
    item = select_by_id(model, id)
    if item:
        db.session.delete_item(item)
        db.session.commit()
        return item
    return False
