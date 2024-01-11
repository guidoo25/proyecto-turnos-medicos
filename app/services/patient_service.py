from app.repositories.patient_repository import PatientRepository

class PatientService:
    def __init__(self):
        self.repository = PatientRepository()

    def get_all_patients(self):
        return self.repository.get_all()

    def get_patient_by_id(self, patient_id):
        return self.repository.get_by_id(patient_id)

    def create_patient(self, patient_data):
        return self.repository.create(patient_data)

    def update_patient(self, patient_id, patient_data):
        return self.repository.update(patient_id, patient_data)

    def delete_patient(self, patient_id):
        return self.repository.delete(patient_id)