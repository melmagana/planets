import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

planets = Blueprint('planets', 'planets')

@planets.route('/', methods=['GET'])
@login_required
def planets_index():
	# result = models.Planet.select()
	# print(result)

	""" get all the planets from the database associated with the currently logged in user """
	current_user_planet_dicts = [model_to_dict(planet) for planet in current_user.planets]
	# planet_dicts = [model_to_dict(planet) for planet in result]

	# for planet_dict in planet_dicts:
	for planet_dict in current_user_planet_dicts:
		planet_dict['found_by'].pop('password')
	# print(planet_dicts)
	print(current_user_planet_dicts)

	return jsonify(data=current_user_planet_dicts, message=f"Successfully found {len(current_user_planet_dicts)} planets", status=200), 200

@planets.route('/', methods=['POST'])
def create_planet():
	payload = request.get_json()
	print(payload)
	add_planet = models.Planet.create(name=payload['name'], planet_type=payload['planet_type'], orbital_period=payload['orbital_period'], moons=payload['moons'], found_by=current_user.id)
	print('- ' * 20)
	print('printed add_planet')
	print(add_planet)
	print('- ' * 20)
	print('printed add_planet.__dict__')
	print(add_planet.__dict__)
	print('- ' * 20)
	print('printed dir(add_planet)')
	print(dir(add_planet))
	# return 'CREATE ROUTE for PLANET running'
	planet_dict = model_to_dict(add_planet)

	#remove password
	planet_dict['found_by'].pop('password')
	return jsonify(data=planet_dict, message='Successfully created a planet!', status=201), 201

@planets.route('/<id>', methods=['DELETE'])
def delete_planet(id):
	delete_query = models.Planet.delete().where(models.Planet.id == id)
	num_rows_deleted = delete_query.execute()
	print('- ' * 20)
	print('printed num_rows_deleted')
	print(num_rows_deleted)
	return jsonify(data={}, message=f'Successfully deleted a planet with the id of {id}!', status=200), 200

@planets.route('/<id>', methods=['PUT'])
def update_planet(id):
	payload = request.get_json()
	update_query = models.Planet.update(name=payload['name'], planet_type=payload['planet_type'], orbital_period=payload['orbital_period'], moons=payload['moons'], found_by=payload['found_by']).where(models.Planet.id == id)

	num_rows_updated = update_query.execute()
	updated_planet = models.Planet.get_by_id(id)
	updated_planet_dict = model_to_dict(updated_planet)

	return jsonify(data={}, message=f'Successfully updated a planet with the id of {id}!', status=200), 200























