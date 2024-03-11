from flask import Flask
from celery import Celery

app = Flask(__name__)

app.config.from_pyfile('config.py')

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
