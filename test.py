import pytest
from flask_testing import TestCase
from run import app

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_certificate_blueprint(self):
        response = self.client.get('/patients')  
        self.assertEqual(response.status_code, 200)

    def test_doctor_blueprint(self):
        response = self.client.get('/doctors')  


if __name__ == '__main__':
    pytest.main()