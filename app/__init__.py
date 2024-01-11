from flask import Flask
from .controllers import patient_controller, doctor_controller, schedule_controller, role_controller, certificate_controller
from flask_sqlalchemy import SQLAlchemy
def create_app():
    app = Flask(__name__)

    app.register_blueprint(patient_controller.bp)
    app.register_blueprint(doctor_controller.bp)
    app.register_blueprint(schedule_controller.bp)
    app.register_blueprint(role_controller.bp)
    app.register_blueprint(certificate_controller.bp)
    db = SQLAlchemy(app)
    

    return app, db