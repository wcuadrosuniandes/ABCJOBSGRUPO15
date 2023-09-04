from flask_restful import Resource
import requests


class RegisterCandidate(Resource):
    def get(self):
        try:
            response = requests.get('http://localhost:5000/register-candidate')
            if response.status_code == 200:
                return response.json(), 200
            else:
                return {'message': 'Error on register API'}, response.status_code
        except Exception as e:
            return {'message': 'Error', 'error': e}, 500
    
    def post(self):
        try:
            response = requests.post('http://localhost:5000/register-candidate')
            if response.status_code == 200:
                return response.json(), 200
            else:
                return {'message': 'Error on register API'}, response.status_code
        except Exception as e:
            return {'message': 'Error', 'error': e}, 500
    