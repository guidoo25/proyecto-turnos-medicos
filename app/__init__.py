from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # La definición de db está aquí

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Cambia la URI de la base de datos aquí
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    db.init_app(app)

    return app