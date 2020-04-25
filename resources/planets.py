import models

from flask import Blueprint, request

planets = Blueprint('planets', 'planets')

@planets.route('/', methods=['GET'])
def planets_index():
	return 'planets resource working'

@planets.route('/', methods=['POST'])
def create_planet():
	payload = request.get_json()
	print(payload)
	add_planet = models.Planet.create(name=payload['name'], planet_type=payload['planet_type'], length_of_year=payload['length_of_year'], moons=payload['moons'])
	print(add_planet)
	return 'CREATE ROUTE for PLANET running'