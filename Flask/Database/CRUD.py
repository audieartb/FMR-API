from flask_pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
from flask import Flask,Response
from .db import db

class CRUD():

    def __init__(self, collection):
        self.__collection = collection
    
    def get_all(self):

        collection = db[self.__collection]
        resp = collection.find()
        json_resp = json_util.dumps(resp)
        return Response(json_resp, status=200, mimetype='application/json')


    def get_one(self, id):
        
        collection = db[self.__collection]
        mongo_resp = collection.find_one({'_id':ObjectId(id)})
        if(not mongo_resp):
            return Response(status=404)
        json_resp = json_util.dumps(mongo_resp)
        return Response(json_resp, status=200, mimetype='application/json')

    def insert(self, data):

        collection = db[self.__collection]
        mongo_resp = collection.insert_one(data)
        json_resp = json_util.dumps({
            'inserted_id': str(mongo_resp.inserted_id)
        })
        return json_resp

    def update(self, data, id):

        collection = db[self.__collection]

        if(collection.find_one({'_id':ObjectId(id)})):

            mongo_resp = collection.update_one(
                {'_id':ObjectId(id)},
                {'$set':data}
            )

            return Response(status=200)
        else:
            return Response(status=404)

    def delete(self, id):

        collection = db[self.__collection]

        if(collection.find_one({'_id':ObjectId(id)})):

            mongo_resp = collection.delete_one({'_id':ObjectId(id)})

            return Response(status=200)
        else:
            return Response(status=404)

        