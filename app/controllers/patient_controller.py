from flask import Flask, request, jsonify,Blueprint
from flasgger import  swag_from
from app import db
from app.models.patient import  Patient




Blueprint_patient = Blueprint('patient', __name__)

@Blueprint_patient.route('/patients', methods=['POST'])
@swag_from({
    'tags': ['Patients'],
    'summary': 'Add a new patient',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'ci': {'type': 'string'},
                    'doctor_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'New patient added',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], last_name=data['last_name'], ci=data['ci'], doctor_id=data['doctor_id'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'New patient added'}), 201

@Blueprint_patient.route('/patients', methods=['GET'])
@swag_from({
    'tags': ['Patients'],
    'summary': 'Get all patients',
    'responses': {
        '200': {
            'description': 'List of patients',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'last_name': {'type': 'string'},
                        'ci': {'type': 'string'},
                        'doctor_id': {'type': 'integer'}
                    }
                }
            }
        }
    }
})
def get_patients():
    patients = Patient.query.all()
    return jsonify([patient.serialize for patient in patients]), 200

@Blueprint_patient.route('/patients/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Patients'],
    'summary': 'Get a patient by ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Patient found',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'ci': {'type': 'string'},
                    'doctor_id': {'type': 'integer'}
                }
            }
        },
        '404': {
            'description': 'Patient not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def get_patient(id):
    patient = Patient.query.get(id)
    if patient is None:
        return jsonify({'message': 'Patient not found'}), 404
    return jsonify(patient.serialize), 200

@Blueprint_patient.route('/patients/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Patients'],
    'summary': 'Update a patient',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'ci': {'type': 'string'},
                    'doctor_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Patient updated',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Patient not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def update_patient(id):
    data = request.get_json()
    patient = Patient.query.get(id)
    if patient is None:
        return jsonify({'message': 'Patient not found'}), 404
    patient.name = data['name']
    patient.last_name = data['last_name']
    patient.ci = data['ci']
    patient.doctor_id = data['doctor_id']
    db.session.commit()
    return jsonify({'message': 'Patient updated'}), 200

@Blueprint_patient.route('/patients/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Patients'],
    'summary': 'Delete a patient',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Patient deleted',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Patient not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def delete_patient(id):
    patient = Patient.query.get(id)
    if patient is None:
        return jsonify({'message': 'Patient not found'}), 404
    db.session.delete(patient)
    db.session.commit()
    return jsonify({'message': 'Patient deleted'}), 200

