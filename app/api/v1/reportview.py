import json
from flask_restful import Resource
from flask import jsonify,make_response,request
from app.api.v1.reportmodel import incidence, myRedflags
import datetime



class MyReports(Resource):

    def __init__(self):
        self.db = incidence
        self.items = myRedflags()
        
    def post (self):
        
        data = request.get_json()
        
        if data["name"].strip() == "" or data["flag"].strip() == "" or data["location"].strip() == "" :
            if data["name"].strip() == "":
                success_message= {
                'status':400,
                'name':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            elif data["flag"].strip() == "":
                success_message= {
                'status':400,
                'flag':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            else :
                success_message= {
                'status':400,
                'location':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)

        elif data["name"] in ['!','?','@','#','%'] or data["location"] in ['!','?','@','#','%'] or data["flag"] in ['!','?','@','#','%']:
            success_message= {
            'status':400,
            'name':'This field cannot be alphanumeric!'
            }
            return make_response(jsonify({
            "message" : success_message

            }),400)

           
            
        elif type(data["name"])!= str or type(data["flag"])!= str or  type(data["location"])!= str :
            if type(data["name"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "message" : success_message
                    }),404)
            elif type(data["flag"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be left blank or Bad choice"
                            }
                return make_response(jsonify({
                    "message" : success_message
                    }),400)
            else :
                success_message= {
                            'status':400,
                            "type": "This field cannot be left blank or Bad choice"
                            }
                return make_response(jsonify({
                    "type" : success_message
                }),400)
        else:
            response = self.items.save(data["name"], data["flag"], data["location"])
            success_message= {
            
            'message':'created a redflag record'
            }
            return make_response(jsonify({
                "status":201,
                "data" : success_message
                }),201)
            
    def get(self):
        response = self.items.get_Redflags()
        return make_response(jsonify({
            "status":200,
            "data" : response
        }),200)

class Reports(Resource):
    def __init__ (self):
        self.db = incidence
        self.items = myRedflags()
    def get(self, RedFlagsid):
        item = self.items.get_RedflagsById(RedFlagsid)

        return make_response(jsonify({
            'status': 200,
            'data':item

        }),200)


    def patch(self, RedFlagsid):
        data = request.get_json()
        if data["name"].strip() == "" or data["comment"].strip() == "" or data["location"].strip() == "" :
            if data["name"].strip() == "":
                success_message= {
                'status':400,
                'name':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            elif data["comment"].strip() == "":
                success_message= {
                'status':400,
                'comment':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            else :
                success_message= {
                'status':400,
                'location':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)

        elif data["name"] in ['!','?','@','#','%'] or data["location"] in ['!','?','@','#','%'] or data["comment"] in ['!','?','@','#','%']:
            success_message= {
            'status':400,
            'name':'This field cannot be alphanumeric!'
            }
            return make_response(jsonify({
            "message" : success_message

            }),400)
        elif type(data["name"])!= str or type(data["comment"])!= str or  type(data["location"])!= str :
            if type(data["name"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "message" : success_message
                    }),400)
            elif type(data["flag"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be left blank or Bad choice"
                            }
                return make_response(jsonify({
                    "message" : success_message
                    }),400)
            else :
                success_message= {
                            'status':400,
                            "type": "This field cannot be left blank or Bad choice"
                            }
                return make_response(jsonify({
                    "type" : success_message
                }),400)
        else:
            response = self.items.patch_RedflagsById(RedFlagsid,data["name"],data["comment"],data["location"])
    
            success_message = {
                'status':200,
                'id' :RedFlagsid,
                'message':'Updates Red-flag location and comment'
            }
            return make_response(jsonify({
                'data':success_message 
            }),200)
    
    def delete(self, RedFlagsid):
        item = self.items.delete_RedflagsById(RedFlagsid)
        
        success_message = {
            "status":200,
            'message':'Red-flag deleted successfully'
        }
        return make_response(jsonify({
            'data':success_message 
            }),200)