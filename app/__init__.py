from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

from app.product_service import ProductService

product_app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.DEBUG)

product_app.testing = True
try:
    load_dotenv()
    client = MongoClient(os.getenv('MONGO_URI'))
except KeyError:
    client = MongoClient('mongodb://database:27017')
database = client.product_db
product_collection = database.product_collection
product_service = ProductService(product_collection)

from app import product_controller
