from datetime import datetime
from database import db

class Schedule(db.Model):
    __tablename__ = 'schedules'

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    appointment_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, doctor_id, patient_id, appointment_date):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.appointment_date = appointment_date

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Schedule.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
