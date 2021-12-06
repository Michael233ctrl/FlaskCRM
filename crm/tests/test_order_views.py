import http

from sqlalchemy import exists

from crm import db
from crm.models import Order
from crm.tests.test_case_base import TestCaseBase


class TestOrderViews(TestCaseBase):

    def test_orders(self):
        self.create_test_order()
        response = self.client.get('/orders')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_update_order(self):
        self.create_test_order()
        response = self.client.get('/update-order/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/update-order/2')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Order.customer_id == 1)).scalar())
        self.assertTrue(db.session.query(exists().where(Order.customer_id == 2)).scalar())

        response_invalid_data = self.client.get('/update-order/11')
        self.assertEqual(response_invalid_data.status_code, http.HTTPStatus.NOT_FOUND)

        order = Order.query.get(1)
        self.assertEqual(order.customer_id, order.product_id)
        data = dict(customer_id=1, product_id=2)
        response = self.send_post_request('/update-order/1', **data)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_order(self):
        self.create_test_order()
        self.assertEqual(db.session.query(Order.id).count(), 2)
        response = self.client.get('/delete-order/1', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(db.session.query(Order.id).count(), 1)

    def test_create_product(self):
        self.create_test_order()
        data = dict(customer=2, product=1)
        response = self.send_post_request('/create-order', **data)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
