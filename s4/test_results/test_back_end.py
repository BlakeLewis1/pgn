import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, routes 
#from application.models import Animal, Fruit, Colour
from os import getenv

def test_password():
    assert routes.password("dog","apple","red",7) == "dogapplered7"