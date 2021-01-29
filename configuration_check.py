from ErrorHandles import logError
from jsonschema import Draft7Validator, validate
from jsonschema.exceptions import ValidationError, SchemaError
import json


def configuration_check(configuration: dict, schema: dict = None) -> bool:

    # Remember: JSON is Javascript Object Notation, therefore list = array and dict = object

    if schema is None:
        with open('default_schema.json', 'r') as file:
            schema = json.load(file)

    try:
        validate(configuration, schema)
        return True
    except ValidationError:
        validator = Draft7Validator(schema)
        errors = sorted(
            validator.iter_errors(configuration),
            key=lambda e: e.path
        )
        error_message = "ValidationError raised performing configuration check."
        error_message += ('\n\t- ' + '\n\t- '.join([str(error.message) for error in errors]))
        logError(error_message)
        return False
    except SchemaError:
        validator = Draft7Validator(schema)
        errors = sorted(
            validator.iter_errors(configuration),
            key=lambda e: e.path
        )
        error_message = "SchemaError raised performing configuration check."
        error_message += ('\n\t- ' + '\n\t- '.join([str(error.message) for error in errors]))
        logError(error_message)
        # Log error, this is a serious error as an invalid schema will entirely
        # halt the program. Need to work out an acceptable response for this.
        return False
