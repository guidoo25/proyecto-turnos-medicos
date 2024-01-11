from flask import request, jsonify
from app.services.role_service import RoleService

role_service = RoleService()

def get_roles():
    roles = role_service.get_all_roles()
    return jsonify([role.to_dict() for role in roles])

def get_role(id):
    role = role_service.get_role_by_id(id)
    if role is None:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify(role.to_dict())

def create_role():
    data = request.get_json()
    role = role_service.create_role(data)
    return jsonify(role.to_dict()), 201

def update_role(id):
    data = request.get_json()
    role = role_service.update_role(id, data)
    if role is None:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify(role.to_dict())

def delete_role(id):
    role = role_service.delete_role(id)
    if role is None:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify({'message': 'Role deleted successfully'})