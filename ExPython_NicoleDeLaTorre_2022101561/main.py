from flask import Flask
from cliente import cliente

app = Flask(__name__)
app.register_blueprint(cliente)

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)