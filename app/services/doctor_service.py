from app.repositories.doctor_repository import DoctorRepository

class DoctorService:
    def __init__(self):
        self.repository = DoctorRepository()

    def get_all_doctors(self):
        return self.repository.get_all()

    def get_doctor_by_id(self, doctor_id):
        return self.repository.get_by_id(doctor_id)

    def create_doctor(self, doctor_data):
        return self.repository.create(doctor_data)

    def update_doctor(self, doctor_id, doctor_data):
        return self.repository.update(doctor_id, doctor_data)

    def delete_doctor(self, doctor_id):
        return self.repository.delete(doctor_id)