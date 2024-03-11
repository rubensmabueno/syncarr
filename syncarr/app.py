from flask import Flask
from celery import Celery
from syncarr.services.scanner_service import ScannerService

app = Flask(__name__)

app.config.from_pyfile('config.py')

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0 * 60, scan_directory_for_videos.s(), name='scan every 15 minutes')


@celery.task
def scan_directory_for_videos():
    ScannerService().execute(app.config['SCAN_DIRECTORY'])
