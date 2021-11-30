from flask import request
from flask_restful import Resource

from crm.service.service import select_all, select_by_id, create, update, delete


class BaseListApi(Resource):

    def __init__(self):
        self.schema = None
        self.model = None

    def get(self):
        return self.schema.dump(select_all(self.model), many=True), 201

    def post(self):
        data = request.json
        product = create(self.model, **data)
        return self.schema.dump(product), 201


class BaseApi(Resource):

    def __init__(self):
        self.schema = None
        self.model = None

    def get(self, id):
        item = self.schema.dump(select_by_id(self.model, id))
        if item:
            return item, 201
        return {'message': f'Item with id:{id} not found!'}, 404

    def put(self, id):
        data = request.json
        if 'id' in data:
            return {'message': "Parameter (id) cannot be updated"}, 404
        item = self.schema.dump(update(self.model, id, **data))
        if item:
            return item, 201
        return {'message': f'Item with id:{id} not found!'}, 404

    def delete(self, id):
        item = delete(self.model, id)
        if item:
            return {'message': f'{item} was successfully deleted!'}, 201
        return {'message': f'Item with id:{id} not found!'}, 404
