# Adding a route (homepage) to our application

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home_page():
	return "Hello World!"

port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
