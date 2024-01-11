from app.models.patient import Patient
from app import db

class PatientRepository:

    @staticmethod
    def get_all():
        return Patient.query.all()

    @staticmethod
    def get_by_id(id):
        return Patient.query.get(id)

    @staticmethod
    def save(patient):
        db.session.add(patient)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(patient):
        db.session.delete(patient)
        db.session.commit()