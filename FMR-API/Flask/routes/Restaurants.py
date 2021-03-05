from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import json_util
from flask import jsonify, Blueprint, request, Response, jsonify
from ..Database.CRUD import CRUD

restaurants_api = Blueprint('restaurants_api', __name__)

@restaurants_api.route('/restaurants', methods=['POST'])
def insert_user():

    if(not request.json):
        return Response(json.dumps({'invalid request - json is empty'}), status=400)

    action = CRUD(collection='restaurants')

    resp =  action.insert(request.json)
    
    return Response(resp, status=200, mimetype='application/json')
   


@restaurants_api.route('/restaurants',methods=['GET'])
def get_restaurants():

    action = CRUD(collection='restaurants')
    response = action.get_all()
    return response
    

@restaurants_api.route('/restaurants/<id>',methods=['GET'])
def get_user_by_id(id):

    action  = CRUD(collection='restaurants')
    response = action.get_one(id)
    return response



@restaurants_api.route('/restaurants/<id>', methods=['DELETE'])
def delete_user(id):
   
    action = CRUD(collection='restaurants')

    response = action.delete(id)

    return response

@restaurants_api.route('/restaurants/<id>', methods=['PUT'])
def update_user(id):
    
    if(not request.json):
        return Response(json.dumps({'invalid request - json is empty'}), status=400)

    data = request.json

    action = CRUD(collection='restaurants')

    mongo_resp = action.update(data= data, id = id)

    return mongo_resp

