simple_charge = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}

simple_charge_two_polygons = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            },
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}


simple_charge_not_a_feature_collection = {
    "geometry": {
        "type": "Polygon",
        "coordinates": [[[291267.338, 93516.097],
                         [291267.912, 93511.326],
                         [291274.679, 93511.974],
                         [291274.132, 93516.65],
                         [291267.338, 93516.097]]]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}

simple_charge_no_geometry = {
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}

simple_charge_valid_author = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "author": {
        "full-name": "Galileo Galilei",
        "email": "galileo.g@digital.landregistry.gov.uk",
        "organisation": "Land Registry"
    }
}

simple_charge_invalid_author = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "author": {}
}

simple_charge_invalid_author_invalid_email = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "author": {
        "full-name": "Galileo Galilei",
        "email": "bad.email",
        "organisation": "Land Registry"
    }
}

simple_charge_invalid_further_information = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": 12,
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}

financial_charge = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Financial",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "amount-originally-secured": "0.20",
    "rate-of-interest": "7000",
    "start-date": "2016-01-11"
}

financial_charge_roi_and_missing_amount = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Financial",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "rate-of-interest": "7000"
}

financial_charge_invalid_roi = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Financial",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "amount-originally-secured": "0.20",
    "rate-of-interest": "None"
}

financial_charge_invalid_amount = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Financial",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "amount-originally-secured": "0.2",
}

s8_charge = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Land compensation",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "land-works-particulars": "The particulars of the land works",
    "land-sold-description": "Description of the land sold",
    "start-date": "2016-01-11"
}

s8_charge_missing_fields = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Land compensation",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}

s52_charge = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Land compensation",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "land-capacity-description": "Freehold",
    "land-compensation-paid": "1000000",
    "land-compensation-amount-type": "Agreed amount",
    "start-date": "2016-01-11"
}

s52_charge_missing_fields = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 4,
    "charge-type": "Land compensation",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}

simple_charge_with_s8_field = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "land-works-particulars": "LWP",
    "start-date": "2016-01-11"
}

simple_charge_with_s52_field = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "land-compensation-paid": "LWP",
    "start-date": "2016-01-11"
}

simple_charge_with_financial_field = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "rate-of-interest": "Interest may be payable",
    "start-date": "2016-01-11"
}

simple_charge_no_sp_or_ins = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "start-date": "2016-01-11"
}

simple_migrated_charge_all_fields = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "migrating-authority": "Robert",
    "old-register-part": "1",
    "migration-supplier": "Dave",
    "start-date": "2016-01-11"
}

simple_migrated_charge_missing_fields = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "migrating-authority": "Robert",
    "migration-supplier": "Dave",
    "start-date": "2016-01-11"
}

simple_charge_legacy_fields = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "old-register-part": "1",
    "start-date": "2016-01-11"
}

simple_migrated_charge_all_fields_bad_part = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "migrating-authority": "Robert",
    "originating-authority-charge-identifier": "1",
    "old-register-part": "RUBBISH",
    "migration-supplier": "Dave",
    "start-date": "2016-01-11"
}

too_much_expiry = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "expiry-date": "2016-01-11",
    "expiry-text": "Seven weeks before the commencement of works"
}

simple_charge_array_provision = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "statutory-provisions": ["The Law"],
    "start-date": "2016-01-11"
}

simple_charge_string_provision = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "statutory-provision": "The Law",
    "start-date": "2016-01-11"
}

lon_charge = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "tribunal-definitive-certificate-date": "2016-01-02",
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-temporary-certificate-date": "2016-01-02",
    "tribunal-temporary-certificate-expiry-date": "2037-01-02"
}

lon_charge_missing_field = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "tribunal-definitive-certificate-date": "2016-01-02",
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-temporary-certificate-date": "2016-01-02",
    "tribunal-temporary-certificate-expiry-date": "2037-01-02"
}

lon_charge_wrong_type = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "tribunal-definitive-certificate-date": "2016-01-02",
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-temporary-certificate-date": "2016-01-02",
    "tribunal-temporary-certificate-expiry-date": "2037-01-02"
}

lon_charge_no_certificates = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
}

lon_charge_temp_cert_no_expiry = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-temporary-certificate-date": "2016-01-02",
}

lon_charge_temp_expiry_no_cert = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-definitive-certificate-date": "2016-01-02",
    "tribunal-temporary-certificate-expiry-date": "2037-01-02"
}

lon_charge_without_position_dimension = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "tribunal-definitive-certificate-date": "2016-01-02",
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-temporary-certificate-date": "2016-01-02",
    "tribunal-temporary-certificate-expiry-date": "2037-01-02"
}

lon_charge_two_addresses = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-geographic-description": "17 Main Street, Place",
    "charge-address": {
        "line-1": "1 The line",
        "postcode": "AA1 1AA",
        "unique-property-reference-number": 123456789098
    },
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "tribunal-definitive-certificate-date": "2016-01-02",
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-temporary-certificate-date": "2016-01-02",
    "tribunal-temporary-certificate-expiry-date": "2037-01-02"
}


lon_charge_absent_uprn = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[291267.338, 93516.097],
                                     [291267.912, 93511.326],
                                     [291274.679, 93511.974],
                                     [291274.132, 93516.65],
                                     [291267.338, 93516.097]]]
                },
                "properties": None,
                "id": "Hello"
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Light obstruction notice",
    "charge-address": {
        "line-1": "1 The line",
        "postcode": "AA1 1AA"
    },
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11",
    "applicant-name": "John Smith",
    "applicant-address": {
        "street": "17 Place Street",
        "town": "Main Town",
        "county": "County Count",
        "postcode": "EX4 7AN",
        "country": "England"
    },
    "servient-land-interest-description": "Freehold owner",
    "structure-position-and-dimension": {
        "height": "Unlimited height",
        "extent-covered": "All of the extent"
    },
    "tribunal-definitive-certificate-date": "2016-01-02",
    "documents-filed": {
        "form-a": [{
            "bucket": "lon",
            "file_id": "form-a",
            "reference": "lon/form-a/sub-directory"
        }],
        "temporary-certificate": [{
            "bucket": "lon",
            "file_id": "temporary-certificate",
            "reference": "lon/temporary-certificate/sub-directory"
        }],
        "definitive-certificate": [{
            "bucket": "lon",
            "file_id": "definitive-certificate",
            "reference": "lon/definitive-certificate/sub-directory"
        }],
    },
    "tribunal-temporary-certificate-date": "2016-01-02",
    "tribunal-temporary-certificate-expiry-date": "2037-01-02"
}

simple_charge_terrible_geo = {
    "geometry": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "id": "1",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                534030,
                                180510
                            ],
                            [
                                534622.5,
                                180522.5
                            ],
                            [
                                534035,
                                179905
                            ],
                            [
                                534652.5,
                                179890
                            ],
                            [
                                534030,
                                180510
                            ]
                        ]
                    ]
                }
            },
            {
                "type": "Feature",
                "properties": {},
                "id": "2",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [
                            534305,
                            180680
                        ],
                        [
                            534305,
                            180680
                        ]
                    ]
                }
            },
            {
                "type": "Feature",
                "properties": {},
                "id": "3",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                534305,
                                180680
                            ],
                            [
                                534305,
                                180680
                            ],
                            [
                                534305,
                                180680
                            ]
                        ]
                    ]
                }
            },
            {
                "type": "Feature",
                "properties": {},
                "id": "4",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [
                            534062.5,
                            180582.5
                        ],
                        [
                            534917.5,
                            180587.5
                        ],
                        [
                            534100,
                            179710
                        ],
                        [
                            534617.5,
                            180960
                        ]
                    ]
                }
            }
        ]
    },
    "registration-date": "2017-03-03",
    "local-land-charge": 3,
    "charge-type": "Planning",
    "charge-sub-category": "Planning notices",
    "charge-geographic-description": "17 Main Street, Place",
    "further-information-location": "Council Offices, Water Dept.",
    "further-information-reference": "XR23232",
    "originating-authority": "Place City Council",
    "instrument": "Deed",
    "start-date": "2016-01-11"
}
