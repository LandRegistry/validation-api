from validation_api.main import app
import unittest
import json


class TestHealth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_health(self):
        self.assertEqual((self.app.get('/health')).status_code, 200)

    def test_no_schema(self):
        payload = {}
        response = self.app.post('/v100000.0/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)
