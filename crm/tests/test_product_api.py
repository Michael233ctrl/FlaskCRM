import http
from sqlalchemy import exists

from crm import db
from crm.models import Product
from crm.tests.test_case_base import TestCaseBase


class TestProductApi(TestCaseBase):

    def test_get_products(self):
        response = self.client.get('/api/products')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_get_product_by_id_success(self):
        response = self.client.get('/api/products/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/api/products/2')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_get_product_by_id_failure(self):
        response = self.client.get('/api/products/11')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        response = self.client.get('/api/products/22')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    def test_post_product_success(self):
        self.assertFalse(db.session.query(exists().where(Product.name == 'Logitech G-Series Gaming Mouse')).scalar())
        data = {"name": "Logitech G-Series Gaming Mouse", "price": 29.99,
                "description": "Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse."}
        response = self.client.post('/api/products', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertTrue(db.session.query(exists().where(Product.name == 'Logitech G-Series Gaming Mouse')).scalar())

    def test_post_product_failure(self):
        data = {"2": "aVNnfs", "qfqf": "sfbdfn", "d": "adfab"}
        response = self.client.post('/api/products', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertIn(b'Invalid data!', response.data)
        self.assertFalse(db.session.query(exists().where(Product.name == 'aVNnfs')).scalar())

    def test_put_product_success(self):
        data = {"name": "Logitech G-Series Gaming Mouse", "price": 29.99,
                "description": "Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse."}
        response = self.client.put('/api/products/1', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Product.name == 'Logitech G-Series Gaming Mouse')).scalar())

    def test_put_product_failure(self):
        data = {"ae9me": "sdvd", "s23me": "wfeg", "wegwe": "dbfbfd", "p6hew45ne": "qrwrb"}
        response = self.client.put('/api/products/1', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertIn(b'Invalid data!', response.data)
        response = self.client.put('/api/products/2221', json=data, content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    def test_delete_product_success(self):
        response = self.client.delete('/api/products/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertFalse(db.session.query(
            exists().where(Product.name == 'Airpods Wireless Bluetooth Headphones')
        ).scalar())

    def test_delete_product_failure(self):
        response = self.client.delete('/api/products/1111')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)