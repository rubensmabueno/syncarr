from flask import Flask
from celery import Celery, Task

from syncarr.config import CELERY_BROKER_URL, SCAN_TASK_SCHEDULE_SEC

app = Flask(__name__)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url=CELERY_BROKER_URL,
            result_backend=CELERY_BROKER_URL,
            task_ignore_result=True,
            beat_schedule={
                "scan-task-every-1-minute": {
                    "task": "syncarr.tasks.scan_task.task",
                    "schedule": SCAN_TASK_SCHEDULE_SEC,
                }
            },
            include=['syncarr.tasks.scan_task']
        ),
    )
    app.config.from_prefixed_env()
    app.extensions["celery"] = celery_init_app(app)
    return app


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    return celery_app
