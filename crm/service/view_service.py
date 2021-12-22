from crm import db


class Service:

    def select_all(self, model):
        db.session.query(model).all()


    def select_by_id(self, model, id):
        return db.session.query(model).get(id)

    def create(self, model, form_data):
        d = {}
        for key, value in form_data.items():
            if hasattr(model, key):
                d[key] = value
        item = model(**d)
        db.session.add(item)
        db.session.commit()

    def update(self, model, data):
        for key, value in data.items():
            if hasattr(model, key):
                setattr(model, key, value)
        db.session.commit()


def select_all(model):
    return db.session.query(model).all()


def select_by_id(model, id):
    return db.session.query(model).get(id)


def create(model, form_data):
    d = {}
    for key, value in form_data.items():
        if hasattr(model, key):
            d[key] = value
    item = model(**d)
    db.session.add(item)
    db.session.commit()


def update(model, data):
    for key, value in data.items():
        if hasattr(model, key):
            setattr(model, key, value)
    db.session.commit()
