from flask import Flask, request, jsonify, g
import logging as logger
from .Routes import users_api, movies_api, restaurants_api
from flask_pymongo import PyMongo
logger.basicConfig(level="DEBUG")


def create_app():
      
   app = Flask(__name__, instance_relative_config=True)
   app.config.from_pyfile('config.py', silent=True)

   app.register_blueprint(movies_api, url_prefix='/api')
   app.register_blueprint(restaurants_api, url_prefix='/api')
   app.register_blueprint(users_api, url_prefix='/api')


   @app.route('/health', methods=['GET'])
   def health():
      return jsonify(alive=True)

   return app 