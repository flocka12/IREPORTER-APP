from flask import Flask
from flask_restful import Api

def appCreate():
    app = Flask(__name__)
    api = Api (app)
    return app
