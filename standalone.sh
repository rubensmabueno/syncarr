#!/bin/bash

# Start Redis server
redis-server --daemonize yes

sleep 30

# Start Celery worker
celery -A syncarr.worker worker --loglevel=info &

# Start Celery beat
celery -A syncarr.worker beat --loglevel=info &

# Start Flask application
python syncarr/manage.py
