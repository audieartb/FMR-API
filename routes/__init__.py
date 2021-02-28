
from flask import Blueprint

routes = Blueprint('routes', __name__)

from .Movies import movies_api
from .Restaurants import restaurants_api
from .User import users_api
mongoUri = 'mongodb+srv://audie-artavia:newmongopass@clustersc-609.ucywa.gcp.mongodb.net/Jumanji?retryWrites=true&w=majority'
