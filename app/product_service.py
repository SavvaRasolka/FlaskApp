class ProductService:
    def __init__(self, collection):
        self.product_collection = collection

    def get_all_products(self):
        return list(self.product_collection.find({}, {'_id': False}))

    def get_product_by_key(self, key):
        return list(self.product_collection.find({str(key): {'$exists': True}}, {'_id': False}))

    def post_product(self, product: dict):
        if self.product_collection.count_documents({list(product.keys())[0]: {'$exists': True}}) == 0:
            return self.product_collection.insert_one(product).acknowledged
        return False

    def put_product(self, product: dict, key):
        product_to_replace = list(self.product_collection.find({str(key): {'$exists': True}}))
        if len(product_to_replace) != 0 and \
                self.product_collection.count_documents({list(product.keys())[0]: {'$exists': True}}) == 0:
            return self.product_collection.replace_one(product_to_replace[0], product)
        return False
