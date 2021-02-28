from bson.json_util import dumps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
import logging
from flask import jsonify, Blueprint, request, current_app, Response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

users_api = Blueprint('users_api', __name__)



@users_api.route('/users', methods=['POST'])
def insert_user():

    if(not request.json):
        return 'bad request',400
    
    _json = request.json
  
    pass_hash = generate_password_hash(_json['password'])

    if(request.method == 'POST'):
        data = {
                'username' : _json['username'],
                'email' : _json['email'],
                'password' : pass_hash,
                'avatar': _json['avatar_uri'],
                'bio': _json['bio']
                }
        mongo = PyMongo(current_app)
        
        insert_resp = mongo.db.users.insert_one(data)
        
        resp = json_util.dumps({
            'insert_id': str(insert_resp.inserted_id)
            }) 
        

        return Response(resp, status=200, mimetype='application/json')
    else:
        error_message = json_util.dumps({
            'error':'invalid data'
        })
        return Response(error_message, status=400)

@users_api.route('/users',methods=['GET'])
def get_users():

    mongo = PyMongo(current_app)

    mongo_resp = mongo.db.users.find()
    response = json_util.dumps(mongo_resp)

    if(mongo_resp):
        return Response(response, mimetype='application/json')
    

@users_api.route('/users/<id>',methods=['GET'])
def get_user_by_id(id):

    mongo = PyMongo(current_app)

    mongo_resp = mongo.db.users.find_one_or_404({'_id':ObjectId(id)})

    response = json_util.dumps(mongo_resp)

    return Response(response, mimetype='application/json')



@users_api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo = PyMongo(current_app)
    
    if(mongo.db.users.find_one({'_id':ObjectId(id)})):
        
        mongo_resp = mongo.db.users.delete_one({'_id':ObjectId(id)})

        return Response(status=200)
    else:
        error_msg = json_util.dumps({
            'error': 'user does not exist'
        })
        return Response(error_msg, status=404)


@users_api.route('/users', methods=['PUT'])
def update_user():
    mongo = PyMongo(current_app)
    _json = request.json
    id = _json['obj_id']
    
    if(mongo.db.users.find_one({'_id':ObjectId(id)})):

        
        mongo_resp = mongo.db.users.update_one({'_id':ObjectId(id)}, {'$set':{
            'username' : _json['username'],
            'email' : _json['email'],
            'avatar': _json['avatar_uri'],
            'bio': _json['bio']
        }})

        return Response(status=200)
    else:
        error_msg = json_util.dumps({
            'error': 'user does not exist'
        })
        return Response(error_msg, status=404)


