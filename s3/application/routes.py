from application import app
import random


@app.route('/animal', methods=['GET'])
def ending():

	list = ['cat','dog','bird','fish','lion','monkey','snake']
	
	return list[random.randrange(6)]

@app.route('/keys', methods=['GET'])
def keys():
	
	list2 = ['#','+','.','*','/','^','~']
	
	return list[random.randrange(6)] 

	rows = session.query(animal).count()
	number = random.randrange(rows)
	result = animal.query.filter_by(id = number)
	word = result.word
	return word