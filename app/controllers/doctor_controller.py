from flask import request, jsonify
from app.services.doctor_service import DoctorService

doctor_service = DoctorService()

def register_doctor_routes(app):
    @app.route('/doctors', methods=['GET'])
    def get_all_doctors():
        doctors = doctor_service.get_all_doctors()
        return jsonify(doctors), 200

    @app.route('/doctors/<int:doctor_id>', methods=['GET'])
    def get_doctor(doctor_id):
        doctor = doctor_service.get_doctor_by_id(doctor_id)
        if doctor is None:
            return jsonify({'error': 'Doctor not found'}), 404
        return jsonify(doctor), 200

    @app.route('/doctors', methods=['POST'])
    def create_doctor():
        doctor_data = request.get_json()
        doctor = doctor_service.create_doctor(doctor_data)
        return jsonify(doctor), 201

    @app.route('/doctors/<int:doctor_id>', methods=['PUT'])
    def update_doctor(doctor_id):
        doctor_data = request.get_json()
        doctor = doctor_service.update_doctor(doctor_id, doctor_data)
        if doctor is None:
            return jsonify({'error': 'Doctor not found'}), 404
        return jsonify(doctor), 200

    @app.route('/doctors/<int:doctor_id>', methods=['DELETE'])
    def delete_doctor(doctor_id):
        doctor = doctor_service.delete_doctor(doctor_id)
        if doctor is None:
            return jsonify({'error': 'Doctor not found'}), 404
        return jsonify({'message': 'Doctor deleted successfully'}), 200