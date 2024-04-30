import mongomock
import unittest
from app.product_service import ProductService


class TestProductService(unittest.TestCase):

    def setUp(self):
        self.mock_client = mongomock.MongoClient()
        self.collection = self.mock_client.test_db.test_collection
        self.product_service = ProductService(self.collection)
        self.docs = [
            {"name1": "object1"},
            {"name2": "object2"},
            {"name3": "object3"}
        ]
        self.collection.insert_many(self.docs)

    def test_get_all_products(self):

        docs_answer = [
            {"name1": "object1"},
            {"name2": "object2"},
            {"name3": "object3"}
        ]

        result = self.product_service.get_all_products()

        self.assertEqual(result, docs_answer)

    def test_get_product_by_key(self):
        self.assertEqual(self.product_service.get_product_by_key(12), [])
        self.assertEqual(self.product_service.get_product_by_key({'lol': 100}), [])
        self.assertEqual(self.product_service.get_product_by_key('name1'), [{'name1': 'object1'}])
        self.assertEqual(self.product_service.get_product_by_key('name3'), [{'name3': 'object3'}])

    def test_post_product(self):
        docs_answer = [
            {"name1": "object1"},
            {"name2": "object2"},
            {"name3": "object3"},
            {"test1": "object1"}
        ]
        self.product_service.post_product({"test1": "object1"})
        self.assertEqual(self.product_service.get_all_products(), docs_answer)

        self.product_service.post_product({"name1": "object1"})
        self.assertEqual(self.product_service.get_all_products(), docs_answer)

    def test_put_product(self):
        docs_answer = [
            {"name4": "object1"},
            {"name2": "object2"},
            {"name3": "object3"}
        ]
        self.product_service.put_product({"name4": "object1"}, "name1")
        self.assertEqual(self.product_service.get_all_products(), docs_answer)
        self.product_service.put_product({"name5": "object1"}, "name1")
        self.assertEqual(self.product_service.get_all_products(), docs_answer)
        self.product_service.put_product({"name3": "object9999"}, "name4")
        self.assertEqual(self.product_service.get_all_products(), docs_answer)


if __name__ == "__main__":
    unittest.main()
