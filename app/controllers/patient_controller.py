from flask import request, jsonify
from app.services.patient_service import PatientService

patient_service = PatientService()

def get_patients():
    patients = patient_service.get_all_patients()
    return jsonify(patients), 200

def get_patient(id):
    patient = patient_service.get_patient_by_id(id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify(patient), 200

def create_patient():
    data = request.get_json()
    patient = patient_service.create_patient(data)
    return jsonify(patient), 201

def update_patient(id):
    data = request.get_json()
    patient = patient_service.update_patient(id, data)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify(patient), 200

def delete_patient(id):
    patient = patient_service.delete_patient(id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify({'message': 'Patient deleted successfully'}), 200