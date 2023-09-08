from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .Base import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    apellido = db.Column(db.String(128))
    correo = db.Column(db.String(128))
    experiencia = db.Column(db.Integer)
    titulo = db.Column(db.String(128))
    universidad = db.Column(db.String(128))

class CandidadateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Candidate
        include_relationships = True
        load_instance = True

    id = fields.String()

