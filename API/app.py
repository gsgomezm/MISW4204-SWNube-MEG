from services.login import LogIn
from services.sing_up import SingUp
from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager
from flask_restful import Api
from models.model import db, engine


app = Flask(__name__)

@app.route('/Task', methods=['GET'])
def process():
   message = f"Hello,! (GET request)"
   return message

@app.route('/REQ1', methods=['POST'])
def process2():
   message = f"Hello,! (POST request)"
   return message



def add_urls(app):
    api = Api(app)
    api.add_resource(LogIn, '/auth/login')
    api.add_resource(SingUp, '/auth/signup')

def create_flask_app():
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'

    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    jwt = JWTManager(app)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        return jwt_data["sub"]
    
    return app

if __name__ == '__main__':
  app =  create_flask_app()
  db.metadata.create_all(engine)
  app.run(debug=True)
  