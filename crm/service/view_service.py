from crm import db


class ServiceDB:
    def __init__(self):
        self.model = None

    def select_all(self, another_model=None):
        if another_model is None:
            return db.session.query(self.model).all()
        return db.session.query(another_model).all()

    def select_by_id(self, id_):
        return db.session.query(self.model).get(id_)

    def create(self, form_data):
        d = {}
        for key, value in form_data.items():
            if hasattr(self.model, key):
                d[key] = value
        item = self.model(**d)
        self.save(item)

    def update(self, form_data):
        for key, value in form_data.items():
            if hasattr(self.model, key):
                setattr(self.model, key, value)
        self.save()

    def delete_item(self, id_):
        item = self.select_by_id(id_)
        if item:
            db.session.delete(item)
            self.save()
            return item
        return False

    @staticmethod
    def save(item=None):
        if item is not None:
            db.session.add(item)
        db.session.commit()
