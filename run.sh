#!/bin/bash
# Simple script to run the Phishify backend service

echo "Starting Phishify Backend Service..."
echo "Service will be available at http://localhost:5000"
echo ""
echo "Available endpoints:"
echo "  GET  /          - Health check"
echo "  GET  /free      - Are you free?"
echo "  GET  /status    - Service status"
echo "  POST /ask       - Ask questions"
echo ""
echo "Press Ctrl+C to stop the service"
echo ""

python app.py