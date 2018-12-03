from flask import Flask 
from flask_restful import Api,Resource

from .api.v1.reportview import MyReports

def appCreate():
    app = Flask(__name__)
    api = Api (app)

    api.add_resource(MyReports,'/POST/red-flags')
    
    return app