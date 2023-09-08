from functools import wraps
import datetime

def monitor_registration_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the wrapped function
        message, response = func(*args, **kwargs)

        # Log errors if the response code is not 200
        if response.status_code != 200:
            # get the message of the response
            error_response = response.json().get('error', '')

            if message['error'] == 'Respuesta vacia del register API':
                error_response = 'Respuesta vacia del register API'

            with open('error.log', 'a') as f:
                f.write(f'{datetime.datetime.now()} - Error: {error_response}\n')

        return message, response.status_code

    return wrapper