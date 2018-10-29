from flask import request, Blueprint, Response
from flask_negotiate import consumes
from validation_api.validation.validation import get_item_errors
from validation_api.app import app
import json

# This is the blueprint object that gets registered into the app in blueprints.py.
validate = Blueprint('validate', __name__)


@validate.route("/validate", methods=["POST"])
@consumes('application/json')
def validate_data():
    app.logger.info('Validate data')
    payload = request.get_json()
    errors = get_item_errors(payload)
    if not errors:
        app.logger.info("Returning validation successful")
        return Response(status=200)
    else:
        app.logger.warning("Returning validation errors")
        return Response(json.dumps(errors), status=400, mimetype='application/json')
