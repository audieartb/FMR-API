from bson.json_util import dumps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import jsonify, Blueprint, request, current_app
from werkzeug.security import generate_password_hash, check_password_hash

restaurants_api = Blueprint('restaurants_api', __name__)

@restaurants_api.route('/restaurants', methods=['GET'])
def get_restaurants():
    return {'message':'sucess getting to rest'}