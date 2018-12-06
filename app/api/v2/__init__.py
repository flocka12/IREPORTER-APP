from flask_restful import Resource,Api
from flask import Blueprint


version_one = Blueprint('api_v2', __name__,url_prefix = '/api/v2')
api = Api(version_two)

