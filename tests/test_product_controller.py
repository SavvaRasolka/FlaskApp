import unittest
from app import product_app


class TestProductController(unittest.TestCase):

    def setUp(self):
        self.client = product_app.test_client()

    def test_get_products(self):
        result = self.client.get('/products')
        self.assertEqual(result.status_code, 200)

    def test_post_products(self):
        result = self.client.post('/products', json={"cucumber2": 100})
        self.assertEqual(result.status_code, 200)

    def test_get_product_by_key(self):
        result = self.client.get('/products/ice-cream')

        self.assertEqual(result.status_code, 200)

    def test_put_product(self):
        result = self.client.put('/products/cucumber', json={'lol': 222})
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
