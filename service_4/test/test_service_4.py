from flask import url_for
from flask_testing import TestCase

from application import app
from application.routes import scout_ratings

class TestBase(TestCase):
    def create_app(self):
        return app

    def test_get_attribute(self):

        for attribute in scout_ratings['attribute']:
            for skill in scout_ratings['skill']:

                content = {'attribute':attribute, 'skill':skill}
                response = self.client.post(url_for('post_rating'), json=content)

                self.assert200(response)

                expected_rating = round((scout_ratings['attribute'][attribute] + scout_ratings['skill'][skill]))
                self.assertEqual(response.json, expected_rating)
