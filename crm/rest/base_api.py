"""
This module defines the following classes:
 - BaseListApi, list API class
 - BaseApi, API class
"""
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from crm.service.service import select_all, select_by_id, create, update, delete


class BaseListApi(Resource):
    """
    Base list API class for Customer, Product, and Order models
    """

    def __init__(self):

        #: Marshmallow schema used for serialization/deserialization
        self.schema = None

        #: Database model
        self.model = None

    def get(self):
        """
        GET request handler for list API.
        Fetches all records from a given model.

        :return: all records in a JSON format with a status code 200
        """
        return self.schema.dump(select_all(self.model), many=True), 200

    def post(self):
        """
        POST request handler for list API.
        Add a new record to the database.

        :return: newly added record in a JSON format with a status code 201
        or a message with status code 400
        """
        try:
            product = create(self.model, request.json)
        except AttributeError:
            return {'message': "Invalid data!"}, 400
        except IntegrityError:
            return {'message': 'Invalid id!'}, 400

        return self.schema.dump(product), 201


class BaseApi(Resource):
    """
    Base API class for Customer, Product, and Order models
    """

    def __init__(self):

        #: Marshmallow schema used for serialization/deserialization
        self.schema = None

        #: Database model
        self.model = None

    def get(self, id):
        """
        GET request handler for API.
        Fetches record from instance id by a given model.

        :param id: instance id by a given model
        :return: record with a given id in JSON format and status code 200
        or a message with status code 404
        """
        item = self.schema.dump(select_by_id(self.model, id))
        if item:
            return item, 200
        return {'message': f'Item with id:{id} not found!'}, 404

    def put(self, id):
        """
        PUT request handler for API
        Find record by a given id and update it.

        :param id: instance id by a given model
        :return: updated record with a given id in JSON format and status code 200
        or a message with status code 400 or 404
        """
        if 'id' in request.json:
            return {'message': "Parameter (id) cannot be updated"}, 400
        try:
            item = self.schema.dump(update(self.model, id, request.json))
        except AttributeError:
            return {'message': "Invalid data!"}, 400
        except ValueError:
            return {'message': f"Item with id:{id} not found!"}, 404
        return item, 200

    def delete(self, id):
        """
        DELETE request handler for API
        Find record by a given id and delete it.

        :param id: instance id by a given model
        :return: a message in JSON format with status code 200 or a message with status code 404
        """
        item = delete(self.model, id)
        if item:
            return {'message': f'{item} was successfully deleted!'}, 200
        return {'message': f'Item with id:{id} not found!'}, 404
