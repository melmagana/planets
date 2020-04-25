import models

from flask import Blueprint

planets = Blueprint('planets', 'planets')

@planets.route('/', methods=['GET'])
def planets_index():
	return 'planets resource working'

@planets.route('/', methods=['POST'])
def create_planet():
	return 'CREATE ROUTE for PLANET running'