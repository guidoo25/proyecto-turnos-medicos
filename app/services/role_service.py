from app.repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self):
        self.role_repository = RoleRepository()

    def get_all_roles(self):
        return self.role_repository.get_all()

    def get_role_by_id(self, role_id):
        return self.role_repository.get_by_id(role_id)

    def create_role(self, role_data):
        return self.role_repository.create(role_data)

    def update_role(self, role_id, role_data):
        return self.role_repository.update(role_id, role_data)

    def delete_role(self, role_id):
        return self.role_repository.delete(role_id)