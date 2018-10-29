from validation_api.main import app
import unittest
import json
import unit_tests.payloads as payloads
from unit_tests.utility import result_contains_at
import copy

lca_error_message = "Only 'land-sold-description' with 'land-works-particulars' or " + \
                    "'land-capacity-description' with 'land-compensation-paid' and " + \
                    "'land-compensation-amount-type' combinations are acceptable"
text_401_chars = ("*longtext*" * 40) + "1"


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_simple_charge(self):
        payload = payloads.simple_charge
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_simple_charge_no_geometry(self):
        payload = payloads.simple_charge_no_geometry
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['location'], '$.')
        self.assertEqual(data[0]['error_message'], "'geometry' is a required property")

    def test_simple_charge_bad_fi(self):
        payload = payloads.simple_charge_invalid_further_information
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['location'], '$.further-information-reference')
        self.assertEqual(data[0]['error_message'], "12 is not of type 'string'")

    def test_financial_charge(self):
        payload = payloads.financial_charge
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_financial_charge_roi_and_missing_amount(self):
        payload = payloads.financial_charge_roi_and_missing_amount
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "'amount-originally-secured' is a required property",
                                  "$.")
        assert result_contains_at(data,
                                  "Additional properties are not allowed ('rate-of-interest' was unexpected)",
                                  "$.")

    def test_financial_charge_invalid_roi(self):
        payload = payloads.financial_charge_invalid_roi
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "'None' does not match",
                                  "$.rate-of-interest")

    def test_financial_charge_roi_words(self):
        payload = copy.deepcopy(payloads.financial_charge_invalid_roi)
        payload['rate-of-interest'] = 'Interest may be payable'
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_financial_charge_roi_numeric(self):
        payload = copy.deepcopy(payloads.financial_charge_invalid_roi)
        payload['rate-of-interest'] = '4.25'
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_financial_charge_invalid_amount(self):
        payload = payloads.financial_charge_invalid_amount
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'0.2' does not match '", "$.amount-originally-secured")

    def test_s8_charge(self):
        payload = payloads.s8_charge
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_lca_s8_with_s52_field(self):
        payload = copy.deepcopy(payloads.s8_charge)
        payload['land-compensation-paid'] = "Invalid"
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "Additional properties are not allowed ('land-compensation-paid' was unexpected)",
                                  "$.")

    def test_s8_charge_missing_fields(self):
        payload = payloads.s8_charge_missing_fields
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'land-capacity-description' is a required property", "$.")
        assert result_contains_at(data, "'land-compensation-amount-type' is a required property", "$.")
        assert result_contains_at(data, "'land-compensation-paid' is a required property", "$.")
        assert result_contains_at(data, "'land-works-particulars' is a required property", "$.")
        assert result_contains_at(data, "'land-sold-description' is a required property", "$.")

    def test_s52_charge(self):
        payload = payloads.s52_charge
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_s52_charge_missing_fields(self):
        payload = payloads.s52_charge_missing_fields
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'land-capacity-description' is a required property", '$.')
        assert result_contains_at(data, "'land-compensation-amount-type' is a required property", '$.')
        assert result_contains_at(data, "'land-compensation-paid' is a required property", '$.')

    def test_invalid_s8_field(self):
        payload = payloads.simple_charge_with_s8_field
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        assert result_contains_at(data,
                                  "Additional properties are not allowed ('land-works-particulars' was unexpected)",
                                  "$.")

    def test_s8_fields_too_large(self):
        payload = copy.deepcopy(payloads.simple_charge_with_s8_field)
        payload['land-works-particulars'] = text_401_chars
        payload['land-sold-description'] = text_401_chars
        payload['charge-type'] = 'Land compensation'
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'{}' is too long".format(text_401_chars), '$.land-works-particulars')
        assert result_contains_at(data, "'{}' is too long".format(text_401_chars), '$.land-sold-description')

    def test_invalid_s52_field(self):
        payload = payloads.simple_charge_with_s52_field
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        assert result_contains_at(data,
                                  "Additional properties are not allowed ('land-compensation-paid' was unexpected)",
                                  "$.")

    def test_lca_s52_invalid_paid(self):
        payload = copy.deepcopy(payloads.s52_charge)
        payload['land-compensation-paid'] = "£100000"
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'£100000' does not match", "$.land-compensation-paid")

    def test_lca_s52_invalid_amount_type(self):
        payload = copy.deepcopy(payloads.s52_charge)
        payload['land-compensation-amount-type'] = "Invalid type"
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'Invalid type' is not one of ['Agreed amount', 'Estimated amount']",
                                  "$.land-compensation-amount-type")

    def test_lca_s52_with_s8_field(self):
        payload = copy.deepcopy(payloads.s52_charge)
        payload['land-sold-description'] = "Invalid"
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "Additional properties are not allowed ('land-sold-description' was unexpected)",
                                  "$.")

    def test_s52_lc_desc_field_too_large(self):
        payload = copy.deepcopy(payloads.simple_charge_with_s52_field)
        payload['land-capacity-description'] = text_401_chars
        payload['charge-type'] = 'Land compensation'
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'{}' is too long".format(text_401_chars), "$.land-capacity-description")

    def test_invalid_financial_field(self):
        payload = payloads.simple_charge_with_financial_field
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        assert result_contains_at(data,
                                  "Additional properties are not allowed ('rate-of-interest' was unexpected)",
                                  "$.")

    def test_migrated_all_fields(self):
        payload = payloads.simple_migrated_charge_all_fields
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_migrated_missing_fields(self):
        payload = payloads.simple_migrated_charge_missing_fields
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'old-register-part' is a required property", "$.")

    def test_legacy_fields(self):
        payload = payloads.simple_charge_legacy_fields
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "['old-register-part']} is not allowed", "$.")
        assert result_contains_at(data, "'migration-supplier' is a required property", "$.")
        assert result_contains_at(data, "'migrating-authority' is a required property", "$.")

    def test_legacy_field_bad_part(self):
        payload = payloads.simple_migrated_charge_all_fields_bad_part
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['location'], '$.old-register-part')
        self.assertIn(' is not one of ', data[0]['error_message'])

    def test_array_provision(self):
        payload = payloads.simple_charge_array_provision
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "Additional properties are not allowed ('statutory-provisions' was unexpected)",
                                  "$.")

    def test_string_provision(self):
        payload = payloads.simple_charge_string_provision
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_simple_charge_valid_author(self):
        payload = payloads.simple_charge_valid_author
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_simple_charge_invalid_author(self):
        payload = payloads.simple_charge_invalid_author
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['location'], '$.author')
        self.assertEqual(data[0]['error_message'], "'full-name' is a required property")
        self.assertEqual(data[1]['location'], '$.author')
        self.assertEqual(data[1]['error_message'], "'organisation' is a required property")

    def test_simple_charge_invalid_author_invalid_email(self):
        payload = payloads.simple_charge_invalid_author_invalid_email
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['location'], '$.author.email')
        self.assertEqual(data[0]['error_message'], "'bad.email' is not a 'email'")

    def test_simple_charge_not_a_feature_collection(self):
        payload = payloads.simple_charge_not_a_feature_collection
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['location'], '$.geometry.type')
        self.assertEqual(data[0]['error_message'], "'Polygon' is not one of ['FeatureCollection']")

    def test_simple_charge_two_polygons(self):
        payload = payloads.simple_charge_two_polygons
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_lon_charge_valid(self):
        payload = payloads.lon_charge
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_lon_charge_missing_field(self):
        payload = payloads.lon_charge_missing_field
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'applicant-name' is a required property", "$.")

    def test_lon_charge_wrong_type(self):
        payload = payloads.lon_charge_wrong_type
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "Additional properties are not allowed", "$.")
        assert result_contains_at(data, "tribunal-temporary-certificate-expiry-date", "$.")
        assert result_contains_at(data, "documents-filed", "$.")
        assert result_contains_at(data, "structure-position-and-dimension", "$.")
        assert result_contains_at(data, "tribunal-temporary-certificate-date", "$.")
        assert result_contains_at(data, "applicant-name", "$.")
        assert result_contains_at(data, "applicant-address", "$.")

    def test_lon_charge_no_certificates(self):
        payload = payloads.lon_charge_no_certificates
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'tribunal-temporary-certificate-expiry-date' is a required property", "$.")
        assert result_contains_at(data, "'tribunal-temporary-certificate-date' is a required property", "$.")
        assert result_contains_at(data, "'tribunal-definitive-certificate-date' is a required property", "$.")

    def test_lon_charge_temp_cert_no_expiry(self):
        payload = payloads.lon_charge_temp_cert_no_expiry
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'tribunal-temporary-certificate-expiry-date' is a required property", "$.")

    def test_lon_charge_temp_expiry_no_cert(self):
        payload = payloads.lon_charge_temp_expiry_no_cert
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data, "'tribunal-temporary-certificate-date' is a required property", "$.")

    def test_too_many_extents(self):
        payload = copy.deepcopy(payloads.simple_charge)

        feature = {"type": "Feature",
                   "geometry": {
                       "type": "Polygon",
                       "coordinates": [
                           [[511076.08598934463, 381319.1389185938],
                            [502935.0162093069, 344754.81621829123],
                            [460299.51643357374, 365124.6766137525],
                            [478395.29646112275, 392099.3797708411],
                            [511076.08598934463, 381319.1389185938]]
                       ]},
                   "properties": {"id": 1}
                   }

        for _ in range(0, 500):
            payload['geometry']['features'].append(feature)

        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(payload['geometry']['features']), 501)
        self.assertEqual(data[0]['error_message'], "Number of extents exceeds permitted maximum of 500")

    def test_servient_unlimited_whole_extent_valid(self):
        payload = copy.deepcopy(payloads.lon_charge_without_position_dimension)
        payload['structure-position-and-dimension'] = {
            'height': 'Unlimited height',
            'extent-covered': 'All of the extent'
        }
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_servient_unlimited_has_units(self):
        payload = copy.deepcopy(payloads.lon_charge_without_position_dimension)
        payload['structure-position-and-dimension'] = {
            'height': 'Unlimited height',
            'units': 'Feet',
            'extent-covered': 'All of the extent'
        }
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  " is not valid under any of the given schemas",
                                  "$.structure-position-and-dimension")

    def test_servient_limited_valid(self):
        payload = copy.deepcopy(payloads.lon_charge_without_position_dimension)
        payload['structure-position-and-dimension'] = {
            'height': '40',
            'units': 'Metres',
            'extent-covered': 'All of the extent'
        }
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_servient_limited_no_units(self):
        payload = copy.deepcopy(payloads.lon_charge_without_position_dimension)
        payload['structure-position-and-dimension'] = {
            'height': '40',
            'extent-covered': 'All of the extent'
        }
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  " is not valid under any of the given schemas",
                                  "$.structure-position-and-dimension")

    def test_servient_all_extent_has_explanatory_text(self):
        payload = copy.deepcopy(payloads.lon_charge_without_position_dimension)
        payload['structure-position-and-dimension'] = {
            'height': '40',
            'units': 'Metres',
            'extent-covered': 'All of the extent',
            'part-explanatory-text': 'Explanation'
        }
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  " is not valid under any of the given schemas",
                                  "$.structure-position-and-dimension")

    def test_servient_part_extent_valid(self):
        payload = copy.deepcopy(payloads.lon_charge_without_position_dimension)
        payload['structure-position-and-dimension'] = {
            'height': '40',
            'units': 'Metres',
            'extent-covered': 'Part of the extent',
            'part-explanatory-text': 'Explanation'
        }
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_servient_part_extent_missing_text(self):
        payload = copy.deepcopy(payloads.lon_charge_without_position_dimension)
        payload['structure-position-and-dimension'] = {
            'height': '40',
            'units': 'Metres',
            'extent-covered': 'Part of the extent'
        }
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  " is not valid under any of the given schemas",
                                  "$.structure-position-and-dimension")

    def test_only_one_address_allowed(self):
        payload = payloads.lon_charge_two_addresses
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        # Schema validation for this condition is really nasty. Not checking message.

    def test_address_no_uprn(self):
        payload = payloads.lon_charge_absent_uprn
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        # Another case where schema-only validation doesn't give us a nice testable error

    def test_sub_category_invalid_charge_type(self):
        payload = copy.deepcopy(payloads.simple_charge)
        payload['charge-type'] = 'Not a valid charge type'

        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        assert result_contains_at(data,
                                  "'Not a valid charge type' is not one of ['Planning', 'Listed building', "
                                  "'Housing', 'Other', 'Land compensation', 'Financial', 'Light obstruction notice']",
                                  "$.charge-type")

    def test_sub_category_missing_charge_sub_category(self):
        payload = copy.deepcopy(payloads.simple_charge)
        del payload['charge-sub-category']

        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "'charge-sub-category' is a required property",
                                  "$.")

    def test_sub_category_invalid_sub_category_type(self):
        payload = copy.deepcopy(payloads.simple_charge)
        payload['charge-sub-category'] = 'Not a valid sub-category'

        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "'Not a valid sub-category' is not one of ['Change a development', ",
                                  "$.charge-sub-category")

    def test_sub_category_mismatching_sub_category(self):
        payload = copy.deepcopy(payloads.simple_charge)
        payload['charge-sub-category'] = 'Smoke control order'

        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        assert result_contains_at(data,
                                  "'Smoke control order' is not one of ['Approval under house in multiple "
                                  "occupation (HMO)', 'Grant', 'Interim certificate under HMO',",
                                  "$.charge-sub-category")

    def test_geometry_validation_ok(self):
        payload = payloads.simple_charge
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_geometry_validation_terrible_geo(self):
        payload = payloads.simple_charge_terrible_geo
        response = self.app.post('/validate', data=json.dumps(payload),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(response.data.decode())
        self.assertTrue({'location': '$.geometry.features[0].geometry',
                         'error_message': 'geometry must be simple and valid'} in data)
        self.assertTrue({'location': '$.geometry.features[1].geometry',
                         'error_message': 'LineStrings must not be zero length'} in data)
        self.assertTrue({'location': '$.geometry.features[1].geometry',
                         'error_message': 'geometry must be simple and valid'} in data)
        self.assertTrue({'location': '$.geometry.features[2].geometry',
                         'error_message': 'geometry must be simple and valid'} in data)
        self.assertTrue({'location': '$.geometry.features[2].geometry',
                         'error_message': 'Polygon must not be zero area'} in data)
        self.assertTrue({'location': '$.geometry.features[3].geometry',
                         'error_message': 'geometry must be simple'} in data)
        self.assertEqual(response.status_code, 400)
