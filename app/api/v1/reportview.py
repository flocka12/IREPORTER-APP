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

        success_message= {
            
            'message':'created a redflag record'
        }
        return make_response(jsonify({
            "My Reports" : success_message


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


    def patch(self, RedFlagsid):
        data = request.get_json()
        response = self.items.patch_RedflagsById(RedFlagsid,data["name"],data["comment"],data["location"])
        success_message = {
            'id' :RedFlagsid,
            'message':'Updates Red-flag location and comment'
        }
        return make_response(jsonify({
            'data':success_message 
        }),200)
    def delete(self, RedFlagsid):
        item = self.items.delete_RedflagsById(RedFlagsid)

        success_message = {
            'id' :RedFlagsid,
            'message':'Red-flag deleted successfully'
        }
        return make_response(jsonify({
            'data':success_message 
        }),200)
