from crm import db


def select_all(model):
    return db.session.query(model).all()


def select_by_id(model, id):
    return db.session.query(model).get(id)


def create(model, **kwargs):
    for k in kwargs:
        if not hasattr(model, k):
            raise AttributeError
    item = model(**kwargs)
    db.session.add(item)
    db.session.commit()
    return item


def update(model, id, **kwargs):
    item = select_by_id(model, id)
    if item:
        for key, value in kwargs.items():
            if not hasattr(item, key):
                raise AttributeError
            setattr(item, key, value)
        db.session.commit()
        return item
    raise ValueError


def delete(model, id):
    item = select_by_id(model, id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return item
    return False
