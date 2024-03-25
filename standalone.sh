#!/bin/bash

# Start Redis server
redis-server --daemonize yes

sleep 30

# Start Celery worker
celery -A syncarr.worker worker --loglevel=info -s /tmp/celerybeat-schedule &

# Start Celery beat
celery -A syncarr.worker beat --loglevel=info -s /tmp/celerybeat-schedule &

# Start Flask application
python syncarr/manage.py
