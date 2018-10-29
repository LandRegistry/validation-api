import os
# RULES OF CONFIG:
# 1. No region specific code. Regions are defined by setting the OS environment variables appropriately to build up the
# desired behaviour.
# 2. No use of defaults when getting OS environment variables. They must all be set to the required values prior to the
# app starting.
# 3. This is the only file in the app where os.environ should be used.

# For logging
FLASK_LOG_LEVEL = os.environ['LOG_LEVEL']

# For health route
COMMIT = os.environ['COMMIT']

# This APP_NAME variable is to allow changing the app name when the app is running in a cluster. So that
# each app in the cluster will have a unique name.
APP_NAME = os.environ['APP_NAME']

SCHEMA_RELATIVE_DIRECTORY = os.environ['SCHEMA_RELATIVE_DIRECTORY']
SCHEMA_FILENAME = os.environ['SCHEMA_FILENAME']
SCHEMA_VERSIONS = os.environ['SCHEMA_VERSIONS'].split(',')

MAX_HEALTH_CASCADE = os.environ['MAX_HEALTH_CASCADE']
MAX_NO_OF_EXTENTS = os.environ['MAX_NO_OF_EXTENTS']

LOGCONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            '()': 'validation_api.extensions.JsonFormatter'
        },
        'audit': {
            '()': 'validation_api.extensions.JsonAuditFormatter'
        }
    },
    'filters': {
        'contextual': {
            '()': 'validation_api.extensions.ContextualFilter'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        },
        'audit_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'audit',
            'filters': ['contextual'],
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'validation_api': {
            'handlers': ['console'],
            'level': FLASK_LOG_LEVEL
        },
        'audit': {
            'handlers': ['audit_console'],
            'level': 'INFO'
        }
    }
}
