from app.models.schedule import Schedule
from app import db

class ScheduleRepository:

    def get_all_schedules(self):
        return Schedule.query.all()

    def get_schedule_by_id(self, id):
        return Schedule.query.get(id)

    def create_schedule(self, schedule):
        db.session.add(schedule)
        db.session.commit()

    def update_schedule(self, schedule):
        db.session.commit()

    def delete_schedule(self, id):
        schedule = self.get_schedule_by_id(id)
        if schedule:
            db.session.delete(schedule)
            db.session.commit()