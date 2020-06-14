import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db 
from application.models import Animal, Fruit, Colour
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app
    
    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()
        fruit1 = Fruit(fruit='apple')
        fruit2 = Fruit(fruit='pineapple')
        fruit3 = Fruit(fruit='mango')
        fruit4 = Fruit(fruit='pear')
        colour1 = Colour(colour='red')
        colour2 = Colour(colour='blue')
        colour3 = Colour(colour='gold')
        colour4 = Colour(colour='black')
        db.session.add(fruit1)
        db.session.add(fruit2)
        db.session.add(fruit3)
        db.session.add(fruit4)
        db.session.add(colour1)
        db.session.add(colour2)
        db.session.add(colour3)
        db.session.add(colour4)




    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('beginning'))
        self.assertEqual(response.status_code, 200)

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('middle'))
        self.assertEqual(response.status_code, 200)