import models

from flask import Blueprint

planets = Blueprint('planets', 'planets')

@planets.route('/')
def planets_index():
	return 'planets resource working'