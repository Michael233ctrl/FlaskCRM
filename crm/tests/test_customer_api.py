import http
from sqlalchemy import exists

from crm import db
from crm.models import Customer
from crm.tests.test_case_base import TestCaseBase


class TestCustomerApi(TestCaseBase):

    def test_get_customers(self):
        response = self.client.get('/api/customers')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_get_customer_by_id_success(self):
        response = self.client.get('/api/customers/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/api/customers/2')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_get_customer_by_id_failure(self):
        response = self.client.get('/api/customers/11')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        response = self.client.get('/api/customers/22')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    def test_post_customer_success(self):
        self.assertFalse(db.session.query(exists().where(Customer.name == 'Jim')).scalar())
        data = {"name": "Jim", "surname": "Smith", "email": "smith@gmail.com", "phone": "230-121-125"}
        response = self.client.post('/api/customers', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertTrue(db.session.query(exists().where(Customer.name == 'Jim')).scalar())

    def test_post_customer_failure(self):
        data = {"2": "Jim", "qfqf": "Smith", "eaasfmail": "smith@gmail.com", "adga": "230-121-125"}
        response = self.client.post('/api/customers', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertIn(b'Invalid data!', response.data)
        self.assertFalse(db.session.query(exists().where(Customer.name == 'Jim')).scalar())

    def test_put_customer_success(self):
        data = {"name": "Donald", "surname": "Peterson", "email": "donald@peterson.com", "phone": "812-123-134"}
        response = self.client.put('/api/customers/1', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Customer.name == 'Donald')).scalar())

    def test_put_customer_failure(self):
        data = {"ae9me": "Donald", "s23me": "Peterson", "2ail": "donald@peterson.com", "p6hew45ne": "812-123-134"}
        response = self.client.put('/api/customers/1', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertIn(b'Invalid data!', response.data)
        response = self.client.put('/api/customers/2221', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    def test_delete_customer_success(self):
        response = self.client.delete('/api/customers/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertFalse(db.session.query(exists().where(Customer.name == 'John')).scalar())

    def test_delete_customer_failure(self):
        response = self.client.delete('/api/customers/1111')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
