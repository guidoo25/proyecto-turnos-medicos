from app.repositories import ScheduleRepository

class ScheduleService:
    def __init__(self):
        self.repository = ScheduleRepository()

    def get_all_schedules(self):
        return self.repository.get_all()

    def get_schedule_by_id(self, id):
        return self.repository.get_by_id(id)

    def create_schedule(self, schedule):
        return self.repository.create(schedule)

    def update_schedule(self, id, schedule):
        return self.repository.update(id, schedule)

    def delete_schedule(self, id):
        return self.repository.delete(id)