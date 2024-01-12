import os

from celery import Celery


def make_celery(app):
    print("RabbitMQ URI:", app.config['CELERY_BROKER_URL'])
    celery_app = Celery(
        app, broker=app.config['CELERY_BROKER_URL'], backend=os.environ.get('CELERY_BACKEND'),
        include=['app.celery_config.celery_task']
    )

    return celery_app
