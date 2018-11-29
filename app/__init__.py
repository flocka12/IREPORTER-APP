from flask import Flask
from flask_restful import Api,Resource

from .api.v1.reportview import MyReports,Reports
from .api.v1.userview import UserRegister

def appCreate():
    app = Flask(__name__)
    api = Api (app)

    api.add_resource(MyReports,'/GET/red-flags')
    api.add_resource(Reports,'/GET/<int:RedFlagsid>')

    api.add_resource(UserRegister,'/Register')
    return app
