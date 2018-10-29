from validation_api.main import app
import unittest
import json
import unit_tests.payloads6 as payloads


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_simple_charge(self):
        payload = payloads.llc_v6_janky_ids
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertIn({'error_message': "'properties' is a required property",
                       'location': '$.geometry.features[0]'}, data)
        self.assertIn({'error_message': "'id' is a required property",
                       'location': '$.geometry.features[1].properties'}, data)
        self.assertIn({'error_message': "'Not a number' is not of type 'integer'",
                       'location': '$.geometry.features[2].properties.id'}, data)
        self.assertIn({'error_message': "Duplicate Feature ID '22'",
                       'location': '$.geometry.features[5].properties.id'}, data)
        self.assertIn({'error_message': '-1 is less than the minimum of 0',
                       'location': '$.geometry.features[6].properties.id'}, data)
        self.assertIn({'error_message': '999999999999999999999999999999999999999999999999999999999999999999999 '
                       'is greater than the maximum of 9223372036854775807',
                       'location': '$.geometry.features[7].properties.id'}, data)
