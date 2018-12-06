from app.api.v1.reportview import MyReports,Reports


from flask_restful import Resource,Api
from flask import Blueprint


version_one = Blueprint('api_v1', __name__,url_prefix = '/api/v1')

api = Api(version_one)

api.add_resource(MyReports,'/red_flags')
api.add_resource(Reports,'/<int:RedFlagsid>')
