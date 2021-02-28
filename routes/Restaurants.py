from bson.json_util import dumps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from flask import jsonify, Blueprint, request, current_app, Response, jsonify, json
from werkzeug.security import generate_password_hash, check_password_hash

restaurants_api = Blueprint('restaurants_api', __name__)

@restaurants_api.route('/restaurants', methods=['POST'])
def insert_user():

    if(not request.json):
        return Response(json.dumps({'invalid request'}), status=400)
    
    _json = request.json
  
    if(request.method == 'POST'):
        data = {
                'name' : _json['name'],
                'style' : _json['style'],
                'location' : _json['location'],
                'rating': _json['rating'],
                'url': _json['url']
                }

        mongo = PyMongo(current_app)
        
        insert_resp = mongo.db.restaurants.insert_one(data)
        
        resp = json_util.dumps({
            'insert_id': str(insert_resp.inserted_id)
            })

        return Response(resp, status=200, mimetype='application/json')
    else:
        error_message = json_util.dumps({
            'error':'invalid data'
        })
        return Response(error_message, status=400)

@restaurants_api.route('/restaurants',methods=['GET'])
def get_restaurants():

    mongo = PyMongo(current_app)

    mongo_resp = mongo.db.restaurants.find()
    response = json_util.dumps(mongo_resp)

    if(mongo_resp):
        return Response(response, mimetype='application/json')
    

@restaurants_api.route('/restaurants/<id>',methods=['GET'])
def get_user_by_id(id):

    mongo = PyMongo(current_app)

    mongo_resp = mongo.db.restaurants.find_one_or_404({'_id':ObjectId(id)})

    response = json_util.dumps(mongo_resp)

    return Response(response, mimetype='application/json')



@restaurants_api.route('/restaurants/<id>', methods=['DELETE'])
def delete_user(id):
    mongo = PyMongo(current_app)
    
    if(mongo.db.restaurants.find_one({'_id':ObjectId(id)})):
        
        mongo_resp = mongo.db.restaurants.delete_one({'_id':ObjectId(id)})

        return Response(status=200)
    else:
        error_msg = json_util.dumps({
            'error': 'restaurant does not exist'
        })
        return Response(error_msg, status=404)


@restaurants_api.route('/restaurants', methods=['PUT'])
def update_user():
    mongo = PyMongo(current_app)
    _json = request.json
    id = _json['obj_id']
    
    if(mongo.db.restaurants.find_one({'_id':ObjectId(id)})):

        
        mongo_resp = mongo.db.restaurants.update_one({'_id':ObjectId(id)}, {'$set':{
                'name' : _json['name'],
                'style' : _json['style'],
                'location' : _json['location'],
                'rating': _json['rating'],
                'url': _json['url']
                }})

        return Response(status=200)
    else:
        error_msg = json_util.dumps({
            'error': 'restaurant does not exist'
        })
        return Response(error_msg, status=404)