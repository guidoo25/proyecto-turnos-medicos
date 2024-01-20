from app import db

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    ci = db.Column(db.String(10), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)  
    doctor = db.relationship('Doctor', primaryjoin='Patient.doctor_id==Doctor.id', backref=db.backref('patients', lazy=True))
    certificates = db.relationship('Certificate', secondary='patient_certificate', backref=db.backref('patients', lazy=True))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'ci': self.ci,
            'doctor_id': self.doctor_id

        }

patient_certificate = db.Table('patient_certificate',
    db.Column('patient_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True),
    db.Column('certificate_id', db.Integer, db.ForeignKey('certificates.id'), primary_key=True)
)