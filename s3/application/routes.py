from application import app, db
from application.models import Animal
import random


@app.route('/animal', methods=['GET'])
def ending():


	length = Animal.query.count()
	rand = random.randint(1, length)
	animalRow = Animal.query.filter_by(id = rand).first()
	animal = animalRow.animal
	return animal



