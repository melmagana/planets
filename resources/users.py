import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def test_user():
	return 'user resource works'


@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()

	# make email and username case insensitive
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	print(payload)

	# logic to see if user exists
	try:
		models.User.get(models.User.email == payload['email'])

		# response
		return jsonify(
			data={},
			message=f"A user with the email {payload['email']} already exists",
			status=401
		), 401

	# logic if user does not exist
	except models.DoesNotExist:

		#scramble password with bcrypt
		pw_hash = generate_password_hash(payload['password'])


		#create user
		create_user = models.User.create(
			username=payload['username'],
			email=payload['email'],
			password=pw_hash
		)

		print(create_user)

		create_user_dict = model_to_dict(create_user)
		print(create_user_dict)

		print(type(create_user_dict['password']))
		# Shouldn't send encrypted password back, so get rid of it
		create_user_dict.pop('password')


		return jsonify(
			data=create_user_dict,
			message=f"Successfully registered user {create_user_dict['email']}",
			status=201
		), 201
