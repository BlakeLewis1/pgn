from application import app, db
from application.models import Fruit, Colour
from flask import Response, request
import random


@app.route('/fruit', methods=['GET'])
def beginning():

	length = Fruit.query.count()
	rand = random.randint(1, length)
	fruitRow = Fruit.query.filter_by(id = rand).first()
	fruit = fruitRow.fruit
	return Response(fruit, mimetype="text/plain")


@app.route('/colour', methods=['GET'])
def middle():

	length = Colour.query.count()
	rand = random.randint(1, length)
	colourRow = Colour.query.filter_by(id = rand).first()
	colour = colourRow.colour
	return colour
