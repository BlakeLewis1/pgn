from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://localhost:5003/randomword')
    print(response)
    password = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    form = AnimalForm()
    animal = animal.query.all()
    if form.validate_on_submit():
        animalData = Animal(
            animal = form.animal.data
        )

        db.session.add(animalData)
        db.session.commit()