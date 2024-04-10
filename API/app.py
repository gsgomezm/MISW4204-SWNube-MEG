from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/REQ1', methods=['GET'])
def process():
   message = f"Hello,! (GET request)"
   return message

@app.route('/REQ1', methods=['POST'])
def process2():
   message = f"Hello,! (POST request)"
   return message


if __name__ == '__main__':
  app.run(debug=True)