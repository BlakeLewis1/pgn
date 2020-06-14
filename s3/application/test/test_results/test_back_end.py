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
        animal1 = Animal(animal='pig')
        animal2 = Animal(animal='fox')
        animal3 = Animal(animal='pigeon')
        animal4 = Animal(animal='tiger')
        db.session.add(animal1)
        db.session.add(animal2)
        db.session.add(animal3)
        db.session.add(animal4)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('ending'))
        self.assertEqual(response.status_code, 200)

