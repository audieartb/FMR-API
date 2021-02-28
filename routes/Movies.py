from flask import request, Flask, Blueprint, Response, current_app as app
from flask_pymongo import PyMongo


movies_api = Blueprint('movies_api', __name__)

@movies_api.route('/movies', methods=['GET'])
def get_movies():

    
    return {'message':f'get'}
    # data = mongo.db.users.find()
    # print(data)
    # return Response(data, mimetype='application/json')


@movies_api.route('/movies/<id>', methods=['GET'])
def get_movie_by_id(id):

    # movie_data.id = id
    # data = movie_data.get_by_id()

    return {'message':f'get by id : {id}'}

@movies_api.route('/movies', methods=['POST'])
def insert_movie():
    
    
    post_data = {
        'username' : request.form['username'],
        'email' : request.form['email'],
        'password' : request.form['password']
    }

    con = app.app_context()

    mongo = PyMongo(con['MONGO_URI'])
    data = mongo.db.users.insert_one(post_data)

    return Response(data, mimetype='application/json')


@movies_api.route('/movies/<id>',methods=['PUT'])
def update_movie(id):

    title = request.form['title']
    length = request.form['length']

    return {'message':f'update movie {id}, title: {title}, {length}'}


@movies_api.route('/movies', methods=['DELETE'])
def delete_movie(id):

    return {}