from flask import Flask, jsonify

from resources.planets import planets

import models

from flask_cors import CORS

DEBUG=True
PORT=8000

app = Flask(__name__)

CORS(planets, origins=['http://localhost:3000'], support_credentials=True)

app.register_blueprint(planets, url_prefix='/api/v1/planets')

@app.route('/')
def hello():
	return 'Hello, Planets!'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)