from flask import request, jsonify, Blueprint
from ..models.schedule import Schedule
from flask import request, jsonify, Blueprint
from ..models.schedule import Schedule

horario_blueprint = Blueprint('horario', __name__) 

@horario_blueprint.route('/horario', methods=['POST'])
def add_schedule():
    """
    neuvo  horario
    ---
    parameters:
        - in: body
          name: body
          schema:
              id: Schedule
              required:
                  - doctor_id
                  - patient_id
                  - appointment_date
              properties:
                  doctor_id:
                      type: integer
                      description: The ID of the doctor
                  patient_id:
                      type: integer
                      description: The ID of the patient
                  appointment_date:
                      type: string
                      format: date-time
                      description: The date and time of the appointment
    responses:
        201:
            description: Schedule added
        400:
            description: Invalid syntax in request body
    """
    data = request.get_json()
    new_schedule = Schedule(doctor_id=data['doctor_id'], patient_id=data['patient_id'], appointment_date=data['appointment_date'])
    new_schedule.save()
    return jsonify({'message': 'New schedule added'}), 201

@horario_blueprint.route('/schedules', methods=['GET'])
#@swag_from('docs/get_schedules.yml')
def get_schedules():
    schedules = Schedule.get_all()
    return jsonify([schedule.serialize for schedule in schedules]), 200

@horario_blueprint.route('/schedules/<int:id>', methods=['DELETE'])
#@swag_from('docs/delete_schedule.yml')
def delete_schedule(id):
    schedule = Schedule.query.get(id)
    if schedule is None:
        return jsonify({'message': 'Schedule not found'}), 404
    schedule.delete()
    return jsonify({'message': 'Schedule deleted'}), 200
