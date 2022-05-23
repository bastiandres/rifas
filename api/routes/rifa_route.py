import json
from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from api.models.rifa_model import Rifa
from api.schema.rifa_schema import RifaSchema

from ..models import db

rifa_api = Blueprint('rifa', __name__)

@rifa_api.get('/')
@swag_from()
def rifas():
    rifaSch = RifaSchema(many=True)
    rifas = Rifa.query.all()
    data = rifaSch.dump(rifas)

    return jsonify(data)

@rifa_api.post('/new')
@swag_from()
def new_rifa():
    nombre = request.get_json()['nombre']
    imagen = request.get_json()['imagen']

    new_rifa = Rifa(
        nombre=nombre,
        imagen=imagen
    )
    try:
        db.session.add(new_rifa)
        db.session.commit()
    except Exception:
        return jsonify(msg="bad save"),401

    return jsonify(msg='OK'),202

