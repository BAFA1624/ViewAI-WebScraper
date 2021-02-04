# Bad responses are handled using requests.models.Response.raise_for_status() [member function]
# This checks the .status_code member attribute of the Response class:
# - If the status code is good it returns None.
# - If the status code is bad (4XX client error, or 5XX server error), it raises the
#   relevant exception.

import sys
import json
from time import ctime

''' 
TODO: 
    - logError lambda function, respective S3 bucket for errors.
'''

def logError(error_message: str, additional_info: dict = None):
    print("I am logging an error")
    error_payload = {
        "message": error_message,
        "time": ctime()
    }
    if additional_info is not None:
        error_payload.update(additional_info)

    # "error_payload" is then passed to lambda function as an event which logs to the relevant
    # folder in an S3 bucket.
    # For now printing to terminal for sake of testing.

    print("Error payload: {}\n{}".format(
        error_payload['message'], error_payload['time']))
    sys.exit()

    return


class InvalidJSONError:
    def __init__(self, filename: str):
        logError(f"Invalid JSON object encountered in {filename}")
