from syncarr.app import app, celery
from syncarr.services.scanner_service import ScannerService


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0 * 60, scan_directory_for_videos.s(), name='scan every 15 minutes')


@celery.task
def scan_directory_for_videos():
    ScannerService().execute(app.config['SCAN_DIRECTORY'])
