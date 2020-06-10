from application import app, db
from application.models import Fruit, Colour
import random


@app.route('/fruit', methods=['GET'])
def beginning():

	length = Fruit.query.count()
	rand = random.randint(1, length)
	fruitRow = Fruit.query.filter_by(id = rand).first()
	fruit = fruitRow.word
	return fruit

	#list = ['apple','pear','melon','mango','orange','grape','banana']
	
	#return list[random.randrange(len(list))]

@app.route('/colour', methods=['GET'])
def middle():

#	list = ['red','yellow','green','blue','orange','gold','black']
	
#	return list[random.randrange(len(list))]

	length = Colour.query.count()
	rand = random.randint(1, length)
	colourRow = Colour.query.filter_by(id = rand).first()
	colour = colourRow.word
	return colour
