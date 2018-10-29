import os
import json
from jsonschema import RefResolver
from importlib import import_module


class SchemaExtension(object):

    def __init__(self, app=None):
        self.resolver = {}
        self.schema = {}
        self.semantic_validators = {}

        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app):
        path = os.path.split(os.path.realpath(__file__))
        app_dir = os.path.split(path[0])[0]
        for version in app.config['SCHEMA_VERSIONS']:
            schema_path = os.path.join(app_dir, app.config['SCHEMA_RELATIVE_DIRECTORY'], version)
            with open(os.path.join(schema_path, app.config['SCHEMA_FILENAME'])) as schema:
                self.schema[version] = json.load(schema)

            app.logger.info('file://' + schema_path + '/', self.schema[version])
            self.resolver[version] = RefResolver('file://' + schema_path + '/', self.schema[version])
            sem_mod = import_module('validation_api.schema.' + version + '.semantics')
            self.semantic_validators[version] = sem_mod.validation_rules
