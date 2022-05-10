from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from application import app
from application.routes import skill

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_skill(self):
        for i in range(20):
            response = self.client.get(url_for('get_skill'))

            self.assert200(response)
            self.assertIn(response.data.decode(), skill)