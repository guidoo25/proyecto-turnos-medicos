from app.models import Certificate
from app.repositories import CertificateRepository

class CertificateService:
    def __init__(self):
        self.repository = CertificateRepository()

    def create_certificate(self, data):
        certificate = Certificate(**data)
        return self.repository.save(certificate)

    def get_certificate(self, id):
        return self.repository.get(id)

    def update_certificate(self, id, data):
        certificate = self.repository.get(id)
        if certificate:
            for key, value in data.items():
                setattr(certificate, key, value)
            return self.repository.save(certificate)
        return None

    def delete_certificate(self, id):
        certificate = self.repository.get(id)
        if certificate:
            return self.repository.delete(certificate)
        return None