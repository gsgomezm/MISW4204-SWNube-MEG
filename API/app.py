from services.login import LogIn
from services.sing_up import SingUp
from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager
from flask_restful import Api
from typing import Any, List
from flask import jsonify
from models.model import db, engine

app = Flask(__name__)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    

    # Check authorization
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return 'Unauthorized', 401

    # Get user ID from token
    token = auth_header.split(' ')[1]
    user_id = decode_token(token)  # Replace with your token decoding logic

    # Get query parameters
    max_results = request.args.get('max')
    order = request.args.get('order')

    # Query tasks from the database based on user ID and parameters
    tasks = query_tasks(user_id, max_results, order)  # Replace with your database query logic

    # Return tasks as JSON
    return jsonify(tasks)

def query_tasks(user_id: str, max_results: int, order: str) -> List[Any]:
        # Replace with your database query logic
        pass
@app.route('/api/tasks/<int:id_task>', methods=['GET'])
def get_task(id_task):
    # Check authorization
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return 'Unauthorized', 401

    # Get user ID from token
    token = auth_header.split(' ')[1]
    user_id = decode_token(token)  # Replace with your token decoding logic

    # Query task from the database based on user ID and task ID
    task = query_task(user_id, id_task)  # Replace with your database query logic

    # Return task as JSON
    return jsonify(task)

def query_task(user_id: str, id_task: int) -> Any:
    # Replace with your database query logic
    pass



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
  