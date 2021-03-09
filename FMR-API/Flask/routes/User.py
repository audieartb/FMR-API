from bson.json_util import dumps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
import logging
from flask import jsonify, Blueprint, request, current_app, Response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..DataAccess.User_DA import User

users_api = Blueprint('users_api', __name__)



@users_api.route('/users', methods=['POST'])
def insert_user():

    if(not request.json):
        return 'bad request',400
    
    _json = request.json
  
    pass_hash = generate_password_hash(_json['password'])

    request.json['password'] = pass_hash
    print(request.json)
    action = User(collection='users')

    response =  action.insert(request.json)
    
    return Response(response, status=200, mimetype='application/json')

@users_api.route('/users',methods=['GET'])
def get_users():

    action = User(collection='users')
    response = action.get_all()
    return response
    

@users_api.route('/users/<id>',methods=['GET'])
def get_user_by_id(id):

    action  = User(collection='users')
    response = action.get_one(id)
    return response

@users_api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    action = User(collection='users')

    response = action.delete(id)

    return response


@users_api.route('/users/<id>', methods=['PUT'])
def update_user(id):
    
    _json = request.json
    
    if(not request.json):
        return Response(json_util.dumps({'invalid request - json is empty'}), status=400)
        
    data = {
        'username' : _json['username'],
        'email' : _json['email'],
        'avatar': _json['avatar_uri'],
        'bio': _json['bio']
    }

    action = User(collection='users')

    response = action.update(data= data, id = id)

    return response


@users_api.route('/users/authenticate', methods=['POST'])
def authenticate_user():
    
    action = User(collection='users')

    response = action.verify_password(
        email =request.form['email'], 
        password = request.form['password'])
    
    return response

@users_api.route('/users/passchange',methods=['POST'])
def change_password():

    action = User(collection='users')

    response = action.change_password(
        email =request.form['email'], 
        password = request.form['password']
    )

    return response