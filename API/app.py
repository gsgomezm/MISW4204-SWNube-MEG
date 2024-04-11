from services.login import LogIn
from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager
import sqlalchemy
from flask_restful import Api

app = Flask(__name__)

@app.route('/Task', methods=['GET'])
def process():
   message = f"Hello,! (GET request)"
   return message

@app.route('/REQ1', methods=['POST'])
def process2():
   message = f"Hello,! (POST request)"
   return message

def connect_db() -> sqlalchemy.engine.base.Engine:
    
    db_host = "34.95.252.108"
    db_user = "postgres"
    db_pass = "$'khs7QF`nykVDF5"
    db_name = "fpv-database"
    db_port = "5432"

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name,
        )
    )
    return pool

db = connect_db()

def add_urls(app):
    api = Api(app)
    api.add_resource(LogIn, '/login')

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
  app.run(debug=True)