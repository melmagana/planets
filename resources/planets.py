import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

planets = Blueprint('planets', 'planets')

@planets.route('/', methods=['GET'])
def planets_index():
	result = models.Planet.select().dicts()
	planets = [planet for planet in result]
	print('- ' * 20)
	print('printed planets in planets_index()')
	print(planets)
	return jsonify(data=planets, message="Successfully created list".format(len(planets)), status=201), 201

	print('- ' * 20)
	print('printed result')
	print(result)
	return 'planets resource working'

@planets.route('/', methods=['POST'])
def create_planet():
	payload = request.get_json()
	print(payload)
	add_planet = models.Planet.create(name=payload['name'], planet_type=payload['planet_type'], length_of_year=payload['length_of_year'], moons=payload['moons'])
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
	update_query = models.Planet.update(name=payload['name'], planet_type=payload['planet_type'], length_of_year=payload['length_of_year'], moons=payload['moons']).where(models.Planet.id == id)

	num_rows_updated = update_query.execute()
	updated_planet = models.Planet.get_by_id(id)
	updated_planet_dict = model_to_dict(updated_planet)

	return jsonify(data={}, message=f'Successfully updated a planet with the id of {id}!', status=200), 200























