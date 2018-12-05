from flask import Flask, Blueprint

from app.api.v1 import version_one as v1


def appCreate():
    app = Flask(__name__)
    app.register_blueprint(v1)
    






    return app
