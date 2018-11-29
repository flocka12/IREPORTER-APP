import json
from flask_restful import Resource
from flask import jsonify,make_response,request
from reportmodel import incidence, myRedflags



class MyReports(Resource):

    def __init__(self):
        self.db = incidence
        self.items = myRedflags()
    def post (self):

        data = request.get_json()

        print(data["name"])

        response = self.items.save(data["name"], data["flag"], data["location"])
        return make_response(jsonify({
            "My Reports" : response
        }),201)
    def get(self):
        response = self.items.get_Redflags()
        return make_response(jsonify({
            "My redflags" : response
        }),200)

class Reports(Resource):
    def __init__ (self):
        self.db = incidence
        self.items = myRedflags()
    def get(self, RedFlagsid):
        item = self.items.get_RedflagsById(RedFlagsid)

        return make_response(jsonify({
            'data':item

        }),200)