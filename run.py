from flasgger import Swagger
from app import create_app, db
from app.controllers.certificate_controller import certificate_blueprint
from app.controllers.doctor_controller import doctor_blueprint
from app.controllers.schedule_controller import horario_blueprint
from app.controllers.patient_controller import Blueprint_patient

app = create_app()  
swagger = Swagger(app)

with app.app_context():
    db.create_all()  

app.register_blueprint(certificate_blueprint)
app.register_blueprint(doctor_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(Blueprint_patient)

if __name__ == '__main__':
    app.run(debug=True)