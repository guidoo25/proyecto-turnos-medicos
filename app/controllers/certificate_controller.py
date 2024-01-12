from flask import Flask, request, jsonify,Blueprint
from flasgger import Swagger, swag_from
from flask_sqlalchemy import SQLAlchemy
from app.models.certificate import db, Certificate
import os


certificate_blueprint = Blueprint('certificate', __name__)



@certificate_blueprint.route('/certificates', methods=['POST'])

def add_certificate():
    data = request.get_json()
    new_certificate = Certificate(doctor_id=data['doctor_id'], patient_id=data['patient_id'], medical_condition=data['medical_condition'], description=data['description'])
    db.session.add(new_certificate)
    db.session.commit()
    return jsonify({'message': 'New certificate added'}), 201

@certificate_blueprint.route('/certificates', methods=['GET'])
#@swag_from('docs/get_certificates.yml')
def get_certificates():
    certificates = Certificate.query.all()
    return jsonify([certificate.serialize for certificate in certificates]), 200

@certificate_blueprint.route('/certificates/<int:id>', methods=['GET'])
#@swag_from('docs/get_certificate.yml')
def get_certificate(id):
    certificate = Certificate.query.get(id)
    if certificate is None:
        return jsonify({'message': 'Certificate not found'}), 404
    return jsonify(certificate.serialize), 200

@certificate_blueprint.route('/certificates/<int:id>', methods=['PUT'])
#@swag_from('docs/update_certificate.yml')
def update_certificate(id):
    data = request.get_json()
    certificate = Certificate.query.get(id)
    if certificate is None:
        return jsonify({'message': 'Certificate not found'}), 404
    certificate.medical_condition = data['medical_condition']
    certificate.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Certificate updated'}), 200

@certificate_blueprint.route('/certificates/<int:id>', methods=['DELETE'])
#@swag_from('docs/delete_certificate.yml')
def delete_certificate(id):
    certificate = Certificate.query.get(id)
    if certificate is None:
        return jsonify({'message': 'Certificate not found'}), 404
    db.session.delete(certificate)
    db.session.commit()
    return jsonify({'message': 'Certificate deleted'}), 200
