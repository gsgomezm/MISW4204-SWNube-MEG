from flask import Flask, render_template, request
from psycopg2 import Error
import psycopg2

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

def close_connection_db(connection, cursor):
    if connection:
        cursor.close()
        connection.close()

if __name__ == '__main__':
  connection_db
  app.run(debug=True)