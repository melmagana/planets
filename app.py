from flask import Flask, jsonify

from resources.planets import planets

import models

DEBUG=True
PORT=8000

app = Flask(__name__)

app.register_blueprint(planets, url_prefix='/api/v1/planets')

@app.route('/')
def hello():
	return 'Hello, Planets!'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)