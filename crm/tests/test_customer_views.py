import http

from sqlalchemy import exists

from crm import db
from crm.models import Customer
from crm.tests.test_case_base import TestCaseBase


class TestCustomerViews(TestCaseBase):

    def test_customers(self):
        response = self.client.get('/customers')
        print(self.app)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_detail_customer(self):
        response = self.client.get('/customers/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Customer.name == 'John')).scalar())
        response = self.client.get('/customers/2')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Customer.name == 'Peter')).scalar())
        response_invalid_data = self.client.get('/customers/11')
        self.assertEqual(response_invalid_data.status_code, http.HTTPStatus.NOT_FOUND)

    def test_edit_customer(self):
        data = dict(name='Donald', surname='Peterson', email='donald@peterson.com', phone='812-123-134')
        response = self.client.post('/customers/1', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Customer.name == 'Donald')).scalar())

    def test_delete_customer(self):
        response = self.client.delete('/delete-customer/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_create_customer(self):
        data = dict(name='Steve', surname='Smith', email='steve@email.com', phone='112-111-222')
        response = self.client.post('/create-customer', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Customer.name == 'Steve')).scalar())
