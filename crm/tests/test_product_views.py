import http

from sqlalchemy import exists

from crm import db
from crm.models import Product
from crm.tests.test_case_base import TestCaseBase


class TestProductViews(TestCaseBase):

    def test_products(self):
        self.create_test_product()
        response = self.client.get('/products')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_detail_product(self):
        self.create_test_product()
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(
            db.session.query(exists().where(Product.name == 'Airpods Wireless Bluetooth Headphones')).scalar()
        )
        response = self.client.get('/products/2')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Product.name == 'Cannon EOS 80D DSLR Camera')).scalar())

        response_invalid_data = self.client.get('/products/11')
        self.assertEqual(response_invalid_data.status_code, http.HTTPStatus.NOT_FOUND)

    def test_edit_product(self):
        self.create_test_product()
        data = dict(name='iPhone 11 Pro 256GB Memory', price=799.99,
                    description='Introducing the iPhone 11 Pro. A transformative triple-camera '
                                'system that adds tons of capability without complexity',
                    )
        response = self.send_post_request('/products/1', **data)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(db.session.query(exists().where(Product.name == 'iPhone 11 Pro 256GB Memory')).scalar())

    def test_delete_product(self):
        self.create_test_product()
        response = self.client.delete('/delete-product/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_create_product(self):
        self.create_test_product()
        data = dict(name='Sony Playstation 4 Pro White Version', price=399.99,
                    description='The ultimate home entertainment center starts with PlayStation. '
                                'Whether you are into gaming, HD movies, television, music',
                    )
        response = self.send_post_request('/create-product', **data)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertTrue(
            db.session.query(exists().where(Product.name == 'Sony Playstation 4 Pro White Version')).scalar()
        )

