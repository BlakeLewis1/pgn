from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class AnimalForm(FlaskForm):
    animal = StringField('Enter an animal',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    submit = SubmitField('Submit Animal')

class FruitForm(FlaskForm):
    fruit = StringField('Enter a Fruit',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    submit = SubmitField('Submit Fruit')

class ColourForm(FlaskForm):
    colour = StringField('Enter a Colour',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    submit = SubmitField('Submit Colour')