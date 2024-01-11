from flask import Blueprint, request
from app.services.certificate_service import CertificateService
from flasgger import swag_from

certificate_controller = Blueprint('certificate_controller', __name__)

@certificate_controller.route('/certificates', methods=['POST'])
@swag_from('../docs/certificate/create_certificate.yml')
def create_certificate():
    data = request.get_json()
    return CertificateService.create_certificate(data)

@certificate_controller.route('/certificates/<int:certificate_id>', methods=['GET'])
@swag_from('../docs/certificate/get_certificate.yml')
def get_certificate(certificate_id):
    return CertificateService.get_certificate(certificate_id)

@certificate_controller.route('/certificates/<int:certificate_id>', methods=['PUT'])
@swag_from('../docs/certificate/update_certificate.yml')
def update_certificate(certificate_id):
    data = request.get_json()
    return CertificateService.update_certificate(certificate_id, data)

@certificate_controller.route('/certificates/<int:certificate_id>', methods=['DELETE'])
@swag_from('../docs/certificate/delete_certificate.yml')
def delete_certificate(certificate_id):
    return CertificateService.delete_certificate(certificate_id)