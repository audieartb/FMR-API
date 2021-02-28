
from flask import Blueprint

routes = Blueprint('routes', __name__)

from .Movies import movies_api
from .Restaurants import restaurants_api
from .User import users_api

