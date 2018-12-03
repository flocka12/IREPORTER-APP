
from flask import Flask
from flask_restful import Api,Resource

from .api.v1.reportview import MyReports,Reports
from .api.v1.userview import UserRegister

def appCreate():
    app = Flask(__name__)
    api = Api (app)

    api.add_resource(MyReports,'/red_flags')
    api.add_resource(Reports,'/<int:RedFlagsid>')

    api.add_resource(UserRegister,'/Register')
    print("I m runnonskudfui")
    return app