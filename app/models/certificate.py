from datetime import datetime
from database import db

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    issue_date = db.Column(db.DateTime, default=datetime.utcnow)
    medical_condition = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __init__(self, doctor_id, patient_id, medical_condition, description):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.medical_condition = medical_condition
        self.description = description
