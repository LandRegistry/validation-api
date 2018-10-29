# Import every blueprint file
from validation_api.views import general
from validation_api.views import validate


def register_blueprints(app):
    """Adds all blueprint objects into the app."""
    app.register_blueprint(general.general)
    app.register_blueprint(validate.validate, url_prefix='')

    # All done!
    app.logger.info("Blueprints registered")
