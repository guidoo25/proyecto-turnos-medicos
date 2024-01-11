from app.models.role import Role
from app import db

class RoleRepository:

    @staticmethod
    def get_all():
        return Role.query.all()

    @staticmethod
    def get_by_id(role_id):
        return Role.query.get(role_id)

    @staticmethod
    def save(role):
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(role):
        db.session.delete(role)
        db.session.commit()