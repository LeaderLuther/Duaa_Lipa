import unittest
from flask import Flask, url_for, request, redirect
from likes_app import login  # assuming the Flask app and login function are defined in app.py

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_login_success(self):
        # Test successful login
        with self.app.test_request_context('/login', method='POST', data={
            'username': 'testuser',
            'password': 'testpassword',
            'submit_button': 'section1'  # assuming there is a submit button named section1
        }):
            response = login()
            self.assertEqual(response.status_code, 302)  # expecting a redirect to /name
            self.assertEqual(response.location, url_for('name', id=1, _external=True))  # assuming User_ID 1 is returned

    def test_login_failure(self):
        # Test failed login
        with self.app.test_request_context('/login', method='POST', data={
            'username': 'testuser',
            'password': 'wrongpassword',
            'submit_button': 'section1'
        }):
            response = login()
            self.assertEqual(response.status_code, 302)  # expecting a redirect back to /login
            self.assertEqual(response.location, url_for('login', _external=True))
            self.assertIn(b'Incorrect username or password', response.data)  # expecting a flash message

if __name__ == '__main__':
    unittest.main()
