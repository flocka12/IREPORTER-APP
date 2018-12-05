import json
from flask_restful import Resource
from flask import jsonify,make_response,request
from app.api.v1.usermodel import User,UserName

class UserRegister(Resource):

    def __init__(self):
        self.db = User
        self.items = UserName()
    def post (self):

        data = request.get_json()
        
        response = self.items.save(data["username"], data["email"], data["phonenumber"])
        return make_response(jsonify({
                    "My Reports" : response
                    }),201)
        
        