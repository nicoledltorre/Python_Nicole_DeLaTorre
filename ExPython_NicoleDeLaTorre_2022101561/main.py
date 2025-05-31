from flask import Flask
from cliente import cliente

app = Flask(__name__)
app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def hello():
    return 'Nicole De La Torre - 2022101561'

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)