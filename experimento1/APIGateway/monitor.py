from flask import request
from functools import wraps
import datetime


def monitor_registration_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the wrapped function
        message, response = func(*args, **kwargs)

        if response.status_code == 200:
            return message, response.status_code

        # Log errors if the response code is not 200
        # get the message of the response
        try:
            json = response.json()

            error_response = json.get("error", "")

            if message["error"] == "Respuesta vacia del register API":
                error_response = "Respuesta vacia del register API"

            with open("error.log", "a") as f:
                f.write(f"{datetime.datetime.now()} - Error: {error_response}\n")
        except request.exceptions.JSONDecodeError:
            with open("error.log", "a") as f:
                f.write(
                    f"{datetime.datetime.now()} - Error: {response.text} - Could not decode json \n"
                )

        return message, response.status_code

    return wrapper
