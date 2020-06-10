from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import AnimalForm, FruitForm, ColourForm
from application.models import Animal, Fruit, Colour
import requests
import random

@app.route('/', methods=['GET', 'POST'])
def home():
    form1 = AnimalForm()
    form2 = FruitForm()
    form3 = ColourForm()

    if form1.validate_on_submit():
        animalData = Animal(
            animal = form1.animal.data
        )
        db.session.add(animalData)

    if form2.validate_on_submit():
        fruitData = Fruit(
            fruit = form2.fruit.data
        )
        db.session.add(fruitData)

    if form3.validate_on_submit():
        colourData = Colour(
            colour = form3.colour.data
        )
        db.session.add(colourData)

    db.session.commit()
    response = requests.get('http://service4:8003/randomword')
    print(response)
    password = response.text
    return render_template('page.html', AnimalForm = form1, FruitForm = form2, ColourForm = form3,  sentence = password, title = 'Home')
"""
@app.route('/animal', methods=['GET', 'POST'])
def animal():
    form = AnimalForm()
    form2 = FruitForm()
    form3 = ColourForm()
    animal = Animal.query.all()
    if form.validate_on_submit():
        animalData = Animal(
            animal = form.animal.data
        )
        db.session.add(animalData)
        db.session.commit()
    
    response = requests.get('http://service4:8003/randomword')
    print(response)
    password = response.text

    return render_template('page.html', AnimalForm = form, FruitForm = form2, ColourForm = form3,  sentence = password, title = 'Home')

@app.route('/fruit', methods=['GET', 'POST'])
def fruit():
    form = FruitForm()
    form1 = AnimalForm()
    form3 = ColourForm()
    fruit = Fruit.query.all()
    if form.validate_on_submit():
        fruitData = Fruit(
            fruit = form.fruit.data
        )

        db.session.add(fruitData)
        db.session.commit()
    
    response = requests.get('http://service4:8003/randomword')
    print(response)
    password = response.text

    return render_template('page.html', AnimalForm = form1, FruitForm = form, ColourForm = form3,  sentence = password, title = 'Home')

@app.route('/colour', methods=['GET', 'POST'])
def colour():
    form = ColourForm()
    form1 = AnimalForm()
    form2 = FruitForm()
    colour = Colour.query.all()
    if form.validate_on_submit():
        colourData = Colour(
            colour = form.colour.data
        )

        db.session.add(colourData)
    db.session.commit()

    response = requests.get('http://service4:8003/randomword')
    print(response)
    password = response.text

    return render_template('page.html', AnimalForm = form1, FruitForm = form2, ColourForm = form,  sentence = password, title = 'Home')
    """