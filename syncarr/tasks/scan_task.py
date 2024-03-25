from celery import shared_task

from syncarr.config import SCAN_DIRECTORY
from syncarr.services.scanner_service import ScannerService


@shared_task
def task():
    ScannerService().execute(SCAN_DIRECTORY)
