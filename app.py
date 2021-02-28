from flask import Flask, request, jsonify, g
import logging as logger
from routes import users_api, movies_api, restaurants_api
from flask_pymongo import PyMongo
logger.basicConfig(level="DEBUG")

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)
mongo = PyMongo(app)

app.register_blueprint(movies_api, url_prefix='/movies')
app.register_blueprint(restaurants_api, url_prefix='/api')
app.register_blueprint(users_api, url_prefix='/api')


@app.route('/health')
def health():
   return jsonify(alive=True)



if __name__ == '__main__':
   logger.debug("Starting the application")
   app.run(host="0.0.0.0",port=5000, debug=True, use_reloader=True)