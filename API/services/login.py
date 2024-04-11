from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource


class LogIn(Resource):

    
    def post(self):
        token_de_acceso = create_access_token(identity=request.json["id"])
        return {"usuario": request.json["usuario"], "token": token_de_acceso}