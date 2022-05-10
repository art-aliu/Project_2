from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from application import app
from application.routes import attribute


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_attribute(self):

        for i in range(20):
            response = self.client.get(url_for('get_attribute'))

            self.assert200(response)
            self.assertIn(response.data.decode(), attribute)