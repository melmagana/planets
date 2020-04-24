from flask import Flask
from flask import Flask, jsonify

DEBUG=True
PORT=8000

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, Planets!'

if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)