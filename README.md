# Validation API

Simple webservice to validate local-land-charge JSON payloads. Separates the domain-specific stuff away from the generic
register.

## Unit tests

The unit tests are contained in the unit_tests folder. [Pytest](http://docs.pytest.org/en/latest/) is used for unit testing. 

To run the unit tests if you are using the common dev-env use the following command:

```bash
docker-compose exec validation-api make unittest
or, using the alias
unit-test validation-api
```

or

```bash
docker-compose exec validation-api make report="true" unittest
or, using the alias
unit-test validation-api -r
```

## Linting

Linting is performed with [Flake8](http://flake8.pycqa.org/en/latest/). To run linting:
```
docker-compose exec validation-api make lint
```

## Endpoints

This application is documented in documentation/swagger.json. This only covers v2.0 of the item schema and is a simplified form.

See `validation-api/schema/vXXX/local-land-charge.json` for the actual item schema.

## Adding new register item schema versions
- Create a new schema version directory; the main schema file must be `local-land-charge.json`
- Don't forget to create a whole new set of unit tests for the new schema version.
- Include a `semantics.py` file for in-code checks. If reusing checks from previous schema versions, import them into this file. Do not copy-paste whole code blocks.
- Add the new version to the `SCHEMA_VERSIONS` environment variable
- Update `llc-schema-dto` package with the relevant transforms to the latest schema version
- Update the client applications as required
