import http
from crm.tests.test_case_base import TestCaseBase


class TestOrderApi(TestCaseBase):

    def test_get_orders(self):
        response = self.client.get('/api/orders')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_get_orders_by_id_success(self):
        response = self.client.get('/api/orders/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/api/orders/2')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_get_orders_by_id_failure(self):
        response = self.client.get('/api/orders/11')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        response = self.client.get('/api/orders/22')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
