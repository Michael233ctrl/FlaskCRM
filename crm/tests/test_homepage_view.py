import http

from crm.tests.test_case_base import TestCaseBase


class TestCustomerViews(TestCaseBase):
    def test_customers(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)