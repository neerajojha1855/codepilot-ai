#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting Django Q Cluster in the background..."
python manage.py qcluster &

echo "Starting Gunicorn Web Server..."
gunicorn CodePilot.wsgi:application --bind 0.0.0.0:$PORT
