from flask import Flask
from flask_restful import Api,Resource

from .api.v1.reportview import MyReports,Reports


def appCreate():
    app = Flask(__name__)
    api = Api (app)

    api.add_resource(MyReports,'/red-flags')
    api.add_resource(Reports,'/<int:RedFlagsid>')

    return app
