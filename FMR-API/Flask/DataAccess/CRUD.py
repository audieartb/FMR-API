from flask_pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
from flask import Flask,Response
from Flask.Database.db import db

class CRUD():

    def __init__(self, collection):
        self.__collection = collection
    
    
    def get_all(self):


        collection = db[self.__collection]
        resp = collection.find()
        if(resp):
            json_resp = json_util.dumps(resp)
            
            return Response(json_resp, status=200, mimetype='application/json')
        else:
            return Response(status=404)

    def get_one(self, id):
        
        collection = db[self.__collection]
        mongo_resp = collection.find_one({'_id':ObjectId(id)})
        
        if(not mongo_resp):
            return Response(status=404)
        json_resp = json_util.dumps(mongo_resp)
        
        return Response(json_resp, status=200, mimetype='application/json')

    def insert(self, data):

        collection = db[self.__collection]
        
        try:

            mongo_resp = collection.insert_one(data)
            json_resp = json_util.dumps({
                'inserted_id': str(mongo_resp.inserted_id)
            })
            return Response(json_resp, status=201)

        except:
            return Response(status=500)


    def update(self, data, id):

        collection = db[self.__collection]

        if(collection.find_one({'_id':ObjectId(id)})):

            try:
                collection.update_one(
                    {'_id':ObjectId(id)},
                    {'$set':data}
                )

                return Response(status=200)
            except:
                return Response(status=500)
        else:
            return Response(status=404)

    def delete(self, id):

        collection = db[self.__collection]

        if(collection.find_one({'_id':ObjectId(id)})):

            try:

                collection.delete_one({'_id':ObjectId(id)})

                return Response(status=200)
            
            except:
                
                return Response(response= json_util.dumps({'error':'error deleting item'}), status=500)

        else:
            return Response(status=404)

        
    def get_collection(self):
        return str(self.__collection)