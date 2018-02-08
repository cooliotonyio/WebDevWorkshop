# Getting a Flask server up and running

from flask import Flask
import os

app = Flask(__name__)

port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))