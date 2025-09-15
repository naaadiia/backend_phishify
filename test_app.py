#!/usr/bin/env python3
"""
Simple tests for the Phishify backend service
"""

import unittest
import json
from app import app

class TestPhishifyBackend(unittest.TestCase):
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_check(self):
        """Test the health check endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'online')
        self.assertIn('timestamp', data)
    
    def test_are_you_free_endpoint(self):
        """Test the /free endpoint specifically for 'are you free?' question"""
        response = self.app.get('/free')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['question'], 'are you free?')
        self.assertEqual(data['answer'], 'Yes, I am free and ready to help!')
        self.assertEqual(data['status'], 'available')
    
    def test_status_endpoint(self):
        """Test the status endpoint"""
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'free')
        self.assertTrue(data['available'])
        self.assertEqual(data['service'], 'Phishify Backend')
    
    def test_ask_endpoint_with_free_question(self):
        """Test asking 'are you free?' via POST"""
        payload = {'question': 'are you free?'}
        response = self.app.post('/ask', 
                                data=json.dumps(payload),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['question'], 'are you free?')
        self.assertIn('free and ready to help', data['answer'])
        self.assertEqual(data['status'], 'available')
    
    def test_ask_endpoint_with_other_question(self):
        """Test asking a different question via POST"""
        payload = {'question': 'Hello there!'}
        response = self.app.post('/ask',
                                data=json.dumps(payload),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['question'], 'Hello there!')
        self.assertIn('phishing detection backend', data['answer'])
    
    def test_ask_endpoint_missing_question(self):
        """Test POST without question parameter"""
        response = self.app.post('/ask',
                                data=json.dumps({}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()