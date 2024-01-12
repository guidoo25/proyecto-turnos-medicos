from app.models.certificate import Certificate
from app import db

class CertificateRepository:

    def get_all(self):
        return Certificate.query.all()

    def get_by_id(self, id):
        return Certificate.query.get(id)

    def save(self, certificate):
        db.session.add(certificate)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, certificate):
        db.session.delete(certificate)
        db.session.commit()

