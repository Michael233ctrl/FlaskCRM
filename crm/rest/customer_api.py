from flask import request
from flask_restful import Resource

from crm.schemas.customer import CustomerSchema
from crm.service.customer_service import select_all, select_by_id, create_customer, update_customer, delete_customer

SCHEMA = CustomerSchema()


class CustomerListApi(Resource):

    def get(self):
        return SCHEMA.dump(select_all(), many=True), 201

    def post(self):
        data = request.json
        customer = create_customer(**data)
        return SCHEMA.dump(customer), 201


class CustomerApi(Resource):

    def get(self, id):
        customer = SCHEMA.dump(select_by_id(id))
        if customer:
            return customer, 201
        return {'message': f'Customer with id:{id} not found!'}, 404

    def put(self, id):
        data = request.json
        customer = SCHEMA.dump(update_customer(id, **data))
        if customer:
            return customer, 201
        return {'message': f'Customer with id:{id} not found!'}, 404

    def delete(self, id):
        customer = delete_customer(id)
        if customer:
            return {'message': f'Customer {customer} was successfully deleted!'}, 201
        return {'message': f'Customer with id:{id} not found!'}, 404
