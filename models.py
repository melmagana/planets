from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('planets.sqlite')

class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()

	class Meta:
		database = DATABASE

class Planet(Model):
	name = CharField()
	planet_type = CharField()
	length_of_year = CharField()
	moons = IntegerField()

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()

	DATABASE.create_tables([User, Planet], safe=True)
	print('Connected to database and created tables if they were not already there')

	DATABASE.close()