from peewee import *

DATABASE = SqliteDatabase('planets.sqlite')

class Planet(Model):
	name = CharField()
	planet_type = CharField()
	length_of_year = IntegerField()
	moons = BooleanField()

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()

	DATABASE.create_tables([Planet], safe=True)
	print('Connected to database and created tables if they were not already there')

	DATABASE.close()