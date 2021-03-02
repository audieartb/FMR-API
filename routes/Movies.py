from flask import request, Flask, Blueprint, Response, current_app as app
from flask_pymongo import PyMongo
from Database.CRUD import CRUD

movies_api = Blueprint('movies_api', __name__)

@movies_api.route('/movies', methods=['POST'])
def insert_user():

    if(not request.json):
        return Response(json.dumps({'invalid request - json is empty'}), status=400)

    action = CRUD(collection='movies')

    resp =  action.insert(request.json)
    
    return Response(resp, status=200, mimetype='application/json')
   


@movies_api.route('/movies',methods=['GET'])
def get_movies():

    action = CRUD(collection='movies')
    response = action.get_all()
    return response
    

@movies_api.route('/movies/<id>',methods=['GET'])
def get_user_by_id(id):

    action  = CRUD(collection='movies')
    response = action.get_one(id)
    return response



@movies_api.route('/movies/<id>', methods=['DELETE'])
def delete_user(id):
   
    action = CRUD(collection='movies')

    response = action.delete(id)

    return response

@movies_api.route('/movies/<id>', methods=['PUT'])
def update_user(id):
    
    if(not request.json):
        return Response(json.dumps({'invalid request - json is empty'}), status=400)
        
    data = request.json

    action = CRUD(collection='movies')

    mongo_resp = action.update(data= data, id = id)

    return mongo_resp