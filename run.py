from flask import Flask
from flasgger import Swagger
from app.controllers.certificate_controller import certificate_blueprint
from app.controllers.doctor_controller import doctor_blueprint
from app.controllers.schedule_controller import horario_blueprint
from app.controllers.patient_controller import Blueprint_patient

app = Flask(__name__)
swagger = Swagger(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' 
app.register_blueprint(certificate_blueprint)
app.register_blueprint(doctor_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(Blueprint_patient)
print ("localhost:5000/apidocs")

if __name__ == '__main__':
    app.run(debug=True)
