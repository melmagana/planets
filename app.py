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


# WORK WITH USER OBJECT WHEN USER IS LOGGED IN
@login_manager.user_loader
def load_user(user_id):
	try:
		print('loading the following user')
		user = models.User.get_by_id(user_id)

		return user

	except models.DoesNotExist:
		return None


# SEND BACK DATA WHEN USER HITS UNAUTHORIZED
@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data={'error': 'User not logged in'},
		message="You must be logged in to access that resource",
		status=401
	), 401


# CORS -- CROSS ORIGIN RESOURCE SHARING
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