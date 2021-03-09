from .CRUD import CRUD
from ..Database.db import db
from flask import Response
from bson.objectid import ObjectId
from bson import json_util
from werkzeug.security import check_password_hash, generate_password_hash
import logging as logger
logger.basicConfig(level="DEBUG")



class User(CRUD):

    def __init__(self, collection):
        CRUD.__init__(self, collection)
        

    def verify_password(self, password, email):
        
        collection = db[self.get_collection()]

        data = collection.find_one({'email':email})
        if(data):
            if(check_password_hash(data['password'],password)):
                return Response(status=200)
            else:
                return Response(status=403)
        else:
            return Response({'error':'user not found'}, status=404)

    def change_password(self, password, email):

        collection = db[self.get_collection()]

        try:
                
            hashed_password = generate_password_hash(password)

            collection.update_one({'email':email},{'$set':{'password':hashed_password}})

            return Response(status=200)
        except:
            return Response(status=500)
