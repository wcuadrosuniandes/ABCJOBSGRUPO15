from flask_restful import Resource
from flask import jsonify, request

import random
from modelos import Candidate, db, CandidadateSchema

class VistaCandidate(Resource):
    def post(self):
        try: 
            if random.randint(0, 100) > 10:
                candidate = Candidate(
                    nombre =  request.json["nombre"],
                    apellido = request.json["apellido"],
                    correo = request.json["correo"],
                    experiencia = request.json["experiencia"],
                    titulo = request.json["titulo"],
                    universidad = request.json["universidad"],
                )
                db.session.add(candidate)
                db.session.commit()
                return jsonify(
                    correo=candidate.correo,
                    mensaje="Candidato creado exitosamente",
                    status="200"
                )
            else:
                option_error = random.randint(1, 3)
                if option_error == 1:
                    return jsonify(
                        correo="",
                        mensaje="Candidato creado exitosamente",
                        status="200"
                    )
                elif option_error == 2:
                    raise ConnectionError('Error en coneccion ')
                else:
                    raise NotImplementedError('El servicio no se encuentra disponible')
        except ConnectionError as e:
            return {'error': 'Servicio RegisterCandidate offline -- ConnectionError -  + str(e)'}, 404
        except Exception as e:
            return {'error': 'Servicio RegisterCandidate - Internal error - ' + str(e)}, 404
       
