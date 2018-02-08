# We upgrade from a simple string to an HTML file

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home_page(name=None):
	if not name:
		name = "World"
	return render_template("home.html", name = name)

port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))