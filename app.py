from flask import Flask, jsonify
from resources.planets import planets
from resources.users import users
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG=True
PORT=8000

app = Flask(__name__)

# SECRET/KEY FOR SESSIONS
app.secret_key = 'Milo is the best puppy in the world! This is not a secret.'
login_manager = LoginManager()
login_manager.init_app(app)

CORS(planets, origins=['http://localhost:3000'], support_credentials=True)
CORS(users, origins=['http://localhost:3000'], support_credentials=True)

app.register_blueprint(planets, url_prefix='/api/v1/planets')
app.register_blueprint(users, url_prefix='/api/v1/users')

@app.route('/')
def hello():
	return 'Hello, Planets!'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)