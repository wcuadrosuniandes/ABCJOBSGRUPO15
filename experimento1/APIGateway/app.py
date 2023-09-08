from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
from monitor import monitor_registration_errors
import requests
import os

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

cors = CORS(app, resources={r"/*": {"origins": "*"}})

host = os.environ.get('HOST', 'localhost')
port = os.environ.get('PORT', '5001')
url = f'http://{host}:{port}'


@app.route('/register-candidate', methods=['GET', 'POST'])
@monitor_registration_errors
def register_candidate():
    data = request.get_json()
    headers = {
        'Content-Type': 'application/json',   
    }

    response = requests.post(f'{url}/candidate', json=data, headers=headers)
    response_code = response.status_code
    response_data = response.json()

    if response_code != 200:
        return {'error': 'Error on register API'}, response
    
    if response_data['correo'] == '':
        response.status_code = 500
        return {'error': 'Respuesta vacia del register API'}, response

    return response_data, response
    
