import json
from flask_restful import Resource
from flask import jsonify,make_response,request
from app.api.v1.reportmodel import incidence, myRedflags
import datetime
import re

class MyReports(Resource):

    def __init__(self):
        self.db = incidence
        self.items = myRedflags()
        
    def post (self):
        data = request.get_json()
        if 'name' not in data or 'flag' not in data or 'location' not in data :
            if 'name' not in data:
                success_message= {
                'status':400,
                'name':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            elif 'flag' not in data:
                success_message= {
                'status':400,
                'flag':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            else:
                success_message= {
                'status':400,
                'location':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
        elif type(data["name"])!= str or type(data["flag"])!= str or type(data["location"])!= str:
            if type(data["name"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "name" : success_message
                    }),400)
            elif type(data["flag"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "flag" : success_message
                    }),400)
            elif type(data["location"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "location" : success_message
                }),400)
        else:
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
                elif data["location"].strip() == "" :
                    success_message= {
                    'status':400,
                    'location':'This field cannot be left blank!'
                    }
                    return make_response(jsonify({
                    "message" : success_message

                    }),400)

            else:
                for x in data["name"]:
                    if x in ['!','?','@','#','%','1','0','2','3','4','5','6','7','8','9']:
                        success_message= {
                        'status':400,
                        'name':'This field cannot have alphanumeric or numbers!'
                        }
                        return make_response(jsonify({
                        "message" : success_message

                        }),400)
                for x in data["location"]:
                    if x in ['!','?','@','#','%','1','0','2','3','4','5','6','7','8','9']:
                        success_message= {
                        'status':400,
                        'location':'This field cannot have alphanumeric or numbers!'
                        }
                        return make_response(jsonify({
                        "message" : success_message

                        }),400)
                for x in ["redflag","intervention"]:
                    if x == data["flag"]:
                        response = self.items.save(data["name"], data["flag"], data["location"])
                        success_message= {
                    
                        'message':'created a redflag record'
                        }
                        return make_response(jsonify({
                        "status":201,
                        "data" : success_message
                        }),201)
                    else:
                        success_message= {
                        'status':400,
                        'flag':'This field should be a redflag or intervention!'
                        }
                        return make_response(jsonify({
                        "message" : success_message

                        }),400)
                
                
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
        if 'name' not in data or 'comment' not in data or 'location' not in data :
            if 'name' not in data:
                success_message= {
                'status':400,
                'name':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            elif 'comment' not in data:
                success_message= {
                'status':400,
                'comment':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
            else:
                success_message= {
                'status':400,
                'location':'This field cannot be left blank!'
                }
                return make_response(jsonify({
                "message" : success_message

                }),400)
        if type(data["name"])!= str or type(data["comment"])!= str or  type(data["location"])!= str :
            if type(data["name"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "name" : success_message
                    }),400)
            elif type(data["comment"])!= str:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "comment" : success_message
                    }),400)
            else:
                success_message= {
                            'status':400,
                            "type": "This field cannot be a number"
                            }
                return make_response(jsonify({
                    "location" : success_message
                }),400)
        else:
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
                elif data["location"].strip() == "":
                    success_message= {
                    'status':400,
                    'location':'This field cannot be left blank!'
                    }
                    return make_response(jsonify({
                    "message" : success_message

                    }),400)
            else:
                for x in data["name"]:
                    if x in ['!','?','@','#','%','1','0','2','3','4','5','6','7','8','9']:
                        success_message= {
                        'status':400,
                        'name':'This field cannot have alphanumeric or numbers!'
                        }
                        return make_response(jsonify({
                        "message" : success_message

                        }),400)
                for x in data["location"]:
                    if x in ['!','?','@','#','%','1','0','2','3','4','5','6','7','8','9']:
                        success_message= {
                        'status':400,
                        'location':'This field cannot have alphanumeric or numbers!'
                        }
                        return make_response(jsonify({
                        "message" : success_message

                        }),400)
                for x in data["comment"]:
                    if x in ['!','?','@','#','%','1','0','2','3','4','5','6','7','8','9']:
                        success_message= {
                        'status':400,
                        'comment':'This field cannot have alphanumeric or numbers!'
                        }
                        return make_response(jsonify({
                        "message" : success_message

                        }),400)
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