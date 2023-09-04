from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from views import RegisterCandidate

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)
api.add_resource(RegisterCandidate, '/register-candidate')
