# 

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home_page(name=None):
	if name:
		return "Hello {}!".format(name)
	else:
		return "Hello World!"

port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))