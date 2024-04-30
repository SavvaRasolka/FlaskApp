from flask import jsonify, request, make_response
from app import product_app
from app import product_service


@product_app.route('/products', methods=['GET', 'POST'])
def get_products():
    if request.method == 'GET':
        products = product_service.get_all_products()
        return jsonify(products)
    elif request.method == 'POST':
        if product_service.post_product(request.json):
            return make_response('Product posted', 200)
        else:
            return make_response('Product not posted', 400)


@product_app.route('/products/<product_key>', methods=['GET', 'PUT'])
def post_products(product_key):
    if request.method == 'GET':
        return jsonify(product_service.get_product_by_key(product_key))
    elif request.method == 'PUT':
        if product_service.put_product(request.json, product_key):
            return make_response('Product replaced', 200)
        else:
            return make_response('Product not updated', 400)
