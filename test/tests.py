import unittest
from flask import Flask
from run import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_certificate_route(self):
        response = self.app.get('/certificate')  # replace with your actual route
        self.assertEqual(response.status_code, 200)

    def test_doctor_route(self):
        response = self.app.get('/doctor')  # replace with your actual route
        self.assertEqual(response.status_code, 200)

    # Add more tests for your other routes

if __name__ == '__main__':
    unittest.main()