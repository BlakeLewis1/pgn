from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('PGN_DB')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
 
db = SQLAlchemy(app)
 
from application import routes