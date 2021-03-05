from bson.json_util import dumps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
import logging
from flask import jsonify, Blueprint, request, current_app, Response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..Database.CRUD import CRUD

users_api = Blueprint('users_api', __name__)



@users_api.route('/users', methods=['POST'])
def insert_user():

    if(not request.json):
        return 'bad request',400
    
    _json = request.json
  
    pass_hash = generate_password_hash(_json['password'])

    request.json['password'] = pass_hash
    print(request.json)
    action = CRUD(collection='users')

    response =  action.insert(request.json)
    
    return Response(response, status=200, mimetype='application/json')

@users_api.route('/users',methods=['GET'])
def get_users():

    action = CRUD(collection='users')
    response = action.get_all()
    return response
    

@users_api.route('/users/<id>',methods=['GET'])
def get_user_by_id(id):

    action  = CRUD(collection='users')
    response = action.get_one(id)
    return response

@users_api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    action = CRUD(collection='users')

    response = action.delete(id)

    return response


@users_api.route('/users/<id>', methods=['PUT'])
def update_user(id):
    
    _json = request.json
    
    if(not request.json):
        return Response(json.dumps({'invalid request - json is empty'}), status=400)
        
    data = {
        'username' : _json['username'],
        'email' : _json['email'],
        'avatar': _json['avatar_uri'],
        'bio': _json['bio']
    }

    action = CRUD(collection='users')

    mongo_resp = action.update(data= data, id = id)

    return mongo_resp


@users_api.route('/passwordchange/<id>', methods=['PUT'])
def update_password(id):
    pass

@users_api.route('/authenticate', methods=['GET'])
def authenticate_user():
    pass