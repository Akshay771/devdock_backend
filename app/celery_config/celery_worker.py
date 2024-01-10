import os

from celery import Celery


def make_celery(app):
    celery_app = Celery(
        app, broker=os.environ.get('CELERY_BROKER'), backend=os.environ.get('CELERY_BACKEND'),
        include=['app.celery_config.celery_task']
    )

    return celery_app
