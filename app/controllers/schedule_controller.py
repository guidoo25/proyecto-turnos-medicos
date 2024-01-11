from flask import Blueprint, request
from app.services.schedule_service import ScheduleService

schedule_controller = Blueprint('schedule_controller', __name__)
schedule_service = ScheduleService()

@schedule_controller.route('/schedules', methods=['GET'])
def get_schedules():
    return schedule_service.get_all_schedules()

@schedule_controller.route('/schedules/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    return schedule_service.get_schedule_by_id(schedule_id)

@schedule_controller.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.get_json()
    return schedule_service.create_schedule(data)

@schedule_controller.route('/schedules/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    data = request.get_json()
    return schedule_service.update_schedule(schedule_id, data)

@schedule_controller.route('/schedules/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    return schedule_service.delete_schedule(schedule_id)