from flask import Flask
from flask_pymongo import pymongo
import os
password = os.environ.get('SECRET_KEY')

CONNECTION_STRING = f'mongodb+srv://audie-artavia:{password}@clustersc-609.ucywa.gcp.mongodb.net/Jumanji?retryWrites=true&w=majority'

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Jumanji')