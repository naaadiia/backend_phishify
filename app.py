#!/usr/bin/env python3
"""
Simple backend service for Phishify
Responds to the question "are you free?"
"""

from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    """Basic health check endpoint"""
    return jsonify({
        'status': 'online',
        'message': 'Phishify backend is running',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/free', methods=['GET'])
def are_you_free():
    """Responds to the question 'are you free?'"""
    return jsonify({
        'question': 'are you free?',
        'answer': 'Yes, I am free and ready to help!',
        'status': 'available',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/status', methods=['GET'])
def status():
    """Returns current status of the service"""
    return jsonify({
        'service': 'Phishify Backend',
        'version': '1.0.0',
        'status': 'free',
        'available': True,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/ask', methods=['POST'])
def ask_question():
    """Accepts questions via POST and responds"""
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Please provide a question'}), 400
    
    question = data['question'].lower().strip()
    
    if 'are you free' in question or 'free' in question:
        return jsonify({
            'question': data['question'],
            'answer': 'Yes, I am free and ready to help with phishing detection!',
            'status': 'available',
            'timestamp': datetime.now().isoformat()
        })
    else:
        return jsonify({
            'question': data['question'],
            'answer': 'I am a phishing detection backend. Ask me if I am free!',
            'status': 'available',
            'timestamp': datetime.now().isoformat()
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)