import os


SCAN_TASK_SCHEDULE_SEC = int(os.environ.get('SCAN_TASK_SCHEDULE_SEC', 10))
SCAN_DIRECTORY = os.environ.get('SCAN_DIRECTORY', 'resources/')
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
DEBUG = os.environ.get('DEBUG', True)
