from application import app
import random


@app.route('/fruit', methods=['GET'])
def beginning():

	list = ['apple','pear','melon','mango','orange','grape','banana']
	
	return list[random.randrange(6)]

@app.route('/colour', methods=['GET'])
def middle():

	list2 = ['red','yellow','green','blue','orange','gold','black']
	
	return list[random.randrange(6)]

	rows = session.query(fruit).count()
	number = random.randrange(rows)
	result = fruit.query.filter_by(id = number)
	word = result.word
	return word

	rows = session.query(colour).count()
	number = random.randrange(rows)
	result = colour.query.filter_by(id = number)
	word = result.word
	return word