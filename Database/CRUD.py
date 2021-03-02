from flask_pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
from flask import Flask,Response

mongo = MongoClient('mongodb+srv://audie-artavia:newmongopass@clustersc-609.ucywa.gcp.mongodb.net/Jumanji?retryWrites=true&w=majority')
database = mongo['Jumanji']


class CRUD():

    def __init__(self, collection):
        self.__collection = collection
    
    def get_all(self):

        collection = database[self.__collection]
        resp = collection.find()
        json_resp = json_util.dumps(resp)
        return Response(json_resp, status=200, mimetype='application/json')


    def get_one(self, id):

        collection = database[self.__collection]
        mongo_resp = collection.find_one_or_404({'_id':ObjectId(id)})
        json_resp = json_util.dumps(mongo_resp)
        return Response(json_resp, status=200, mimetype='application/json')

    def insert(self, data):

        collection = database[self.__collection]
        mongo_resp = collection.insert_one(data)
        json_resp = json_util.dumps({
            'inserted_id': str(mongo_resp.inserted_id)
        })
        return json_resp

    def update(self, data, id):

        collection = database[self.__collection]

        if(collection.find_one({'_id':ObjectId(id)})):

            mongo_resp = collection.update_one(
                {'_id':ObjectId(id)},
                {'$set':data}
            )

            return Response(status=200)
        else:
            return Response(status=404)

    def delete(self, id):

        collection = database[self.__collection]

        if(collection.find_one({'_id':ObjectId(id)})):

            mongo_resp = collection.delete_one({'_id':ObjectId(id)})

            return Response(status=200)
        else:
            return Response(status=404)

        