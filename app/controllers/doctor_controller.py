from flask import Blueprint, request, jsonify
from app.models.doctor import Doctor

doctor_blueprint = Blueprint('doctor', __name__)

@doctor_blueprint.route('/doctors', methods=['POST'])
def create_doctor():
    """
    Crear a nuevo doctor.
    ---
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - nombre
            - Espicialidad
          properties:
            name:
              type: string
              description: The name of the doctor.
            specialty:
              type: string
              description: The specialty of the doctor.
    responses:
      201:
        description: Doctor created successfully.
    """
    data = request.get_json()
    new_doctor = Doctor(name=data['name'], specialty=data['specialty'])
    new_doctor.save()
    return jsonify({'message': 'Doctor created successfully'}), 201

@doctor_blueprint.route('/doctors', methods=['GET'])
def get_all_doctors():
        """
        Get all doctors.
        ---
        responses:
            200:
                description: List of doctors.
        """
        doctors = Doctor.get_all()
        return jsonify([doctor.serialize for doctor in doctors]), 200

@doctor_blueprint.route('/doctors/<int:id>', methods=['GET'])
def get_doctor_by_id(id):
    """
    Get a doctor by ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the doctor.
    responses:
      200:
        description: Doctor found.
      404:
        description: Doctor not found.
    """
    doctor = Doctor.get_by_id(id)
    if doctor:
        return jsonify(doctor.serialize), 200
    else:
        return jsonify({'message': 'Doctor not found'}), 404

@doctor_blueprint.route('/doctors/<int:id>', methods=['DELETE'])
def delete_doctor(id):
    """
    Delete a doctor by ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the doctor.
    responses:
      200:
        description: Doctor deleted successfully.
      404:
        description: Doctor not found.
    """
    doctor = Doctor.get_by_id(id)
    if doctor:
        doctor.delete()
        return jsonify({'message': 'Doctor deleted successfully'}), 200
    else:
        return jsonify({'message': 'Doctor not found'}), 404