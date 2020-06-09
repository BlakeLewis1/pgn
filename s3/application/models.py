from application import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20), nullable = False)
 
class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(10), nullable = False)
 
class Colour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(10), nullable = False)