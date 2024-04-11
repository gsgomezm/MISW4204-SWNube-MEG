from flask import Flask, render_template, request
from psycopg2 import Error
import psycopg2
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

def connection_db():
    try:
        connection = psycopg2.connect(
            user="root",
            password="2534946",
            host="localhost",
            port="5432",
            database="fpvdb"
        )
        cursor = connection.cursor()
        print("Conexión exitosa a PostgreSQL")
        return connection, cursor
    except (Exception, Error) as error:
        print("Error al conectar a PostgreSQL:", error)
def add_urls(app):
    api = Api(app)
    api.add_resource(LogIn, '/login')

def create_flask_app():
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'

    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    jwt = JWTManager(app)

def close_connection_db(connection, cursor):
    if connection:
        cursor.close()
        connection.close()

if __name__ == '__main__':
  connection_db
  app.run(debug=True)