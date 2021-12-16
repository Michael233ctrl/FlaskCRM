import http

from crm.tests.test_case_base import TestCaseBase


class TestHandlingErrorViews(TestCaseBase):
    def test_page_not_found(self):
        response = self.client.get('/sadqwd')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        self.assertIn(b'404 Not Found', response.data)
        response = self.client.get('/customers/1232')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        self.assertIn(b'404 Not Found', response.data)
