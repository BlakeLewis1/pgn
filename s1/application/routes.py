from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import AnimalForm, FruitForm, ColourForm
from application.models import Animal, Fruit, Colour
import requests
import random

@app.route('/', methods=['GET'])
def home():
    form1 = AnimalForm()
    form2 = FruitForm()
    form3 = ColourForm()

    response = requests.get('http://service4:8003/randomword')
    print(response)
    password = response.text
    return render_template('page.html', AnimalForm = form1, FruitForm = form2, ColourForm = form3,  sentence = password, title = 'Home')

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    form = AnimalForm()
    animal = Animal.query.all()
    if form.validate_on_submit():
        animalData = Animal(
            animal = form.animal.data
        )

        db.session.add(animalData)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/fruit', methods=['GET', 'POST'])
def fruit():
    form = FruitForm()
    fruit = Fruit.query.all()
    if form.validate_on_submit():
        fruitData = Fruit(
            fruit = form.fruit.data
        )

        db.session.add(fruitData)
        db.session.commit()

    return redirect(url_for('home'))

@app.route('/colour', methods=['GET', 'POST'])
def colour():
    form = ColourForm()
    colour = Colour.query.all()
    if form.validate_on_submit():
        colourData = Colour(
            colour = form.colour.data
        )

        db.session.add(colourData)
        db.session.commit()

    return redirect(url_for('home'))