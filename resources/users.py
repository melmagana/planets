import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

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


		# logs in user and starts a session
		login_user(create_user)


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



@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()


	# logic to look up user by email
	try:
		user = models.User.get(models.User.email == payload['email'])

		# user with this email exists

		user_dict = model_to_dict(user)

		# check password using bcrypt
		password_is_good = check_password_hash(user_dict['password'], payload['password'])

		# logic if password is good
		if(password_is_good):

			# log the user in
			login_user(user)

			print(f"{current_user.username} is current_user.username in POST login")
			print(model_to_dict(user))

			# Remove password
			user_dict.pop('password')

			#response
			return jsonify(
				data=user_dict,
				message=f"Successfully logged in {user_dict['email']}",
				status=200
			), 200


		# logic if password is bad
		else:
			print('password is invalid')

			# Response if email or password is invalid
			return jsonify(
				data={},
				message="Email or password is incorrect",
				status=401
			), 401


	# logic if they don't exist
	except models.DoesNotExist:
		print('username is invalid')

		return jsonify(
			data={},
			message="Email or password is invalid",
			status=401
		), 401


# -- HELPFUL ROUTES BEGIN -- #
@users.route('/all', methods=['GET'])
def user_index():
	users = models.User.select()
	user_dicts = [model_to_dict(user) for user in users]

	# remove password
	for user_dict in user_dicts:
		user_dict.pop('password')
	print(user_dicts)
	return jsonify(user_dicts), 200


@users.route('/logged_in_user', methods=['GET'])
def get_logged_in_user():
	print(current_user)
	
	# Logic if user IS NOT currently logged in
	if not current_user.is_authenticated:
		return jsonify(
			data={},
			message="No user is currently logged in",
			status=401
		), 401

	# Logic if user IS currently logged in
	else:
		user_dict = model_to_dict(current_user)

		# Remove password
		user_dict.pop('password')

		return jsonify(
			data=user_dict,
			message=f"Currently logged in as {user_dict['email']}",
			status=200
		), 200



@users.route('/logout', methods=['GET'])
def logout():
	logout_user()

	return jsonify(
		data={},
		message="Successfully logged out!",
		status=200
	), 200



