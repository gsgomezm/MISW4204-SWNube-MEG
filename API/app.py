from asyncio import Task
from services.login import LogIn
from services.sing_up import SingUp
from services.task import Task
from services.task_id import Task_Id
from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager, decode_token
from flask_restful import Api
from typing import Any, List
from flask import jsonify
from models.model import db, engine,User,db_session


app = Flask(__name__)



def add_urls(app):
    api = Api(app)
    api.add_resource(LogIn, '/auth/login')
    api.add_resource(SingUp, '/auth/signup')
    api.add_resource(Task, '/task')
    api.add_resource(Task_Id, '/task/<int:id_task>')
  

def create_flask_app():
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'

    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    jwt = JWTManager(app)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return db_session.query(User).filter(User.id==identity).first()
    
    return app

if __name__ == '__main__':
  app =  create_flask_app()
  db.metadata.create_all(engine)
  app.run(debug=True)
  
