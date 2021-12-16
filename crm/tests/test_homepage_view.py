import http

from crm.tests.test_case_base import TestCaseBase


class TestHomepageViews(TestCaseBase):
    def test_dashboard(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_search_success(self):
        response = self.client.get('/search?q=Airpods')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertIn(b'Airpods Wireless Bluetooth Headphones', response.data)
        response = self.client.get('/search?q=Camera')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertIn(b'Cannon EOS 80D DSLR Camera', response.data)

    def test_search_failure(self):
        response = self.client.get('/search?q=as12dassf')
        self.assertIn(b'No results!', response.data)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/search')
        self.assertIn(b'No results!', response.data)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
