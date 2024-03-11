#!/bin/bash

# Start Redis server
redis-server --daemonize yes

# Start Celery worker
celery -A app.celery worker --loglevel=INFO &

# Start Flask application
gunicorn --workers=4 --bind=0.0.0.0:5000 syncarr:app
