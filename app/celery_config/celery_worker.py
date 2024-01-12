import os

from celery import Celery


def make_celery(app):
    print("RabbitMQ URI:", app.config['CELERY_BROKER_URL'])
    celery_app = Celery(
        app, broker=app.config['CELERY_BROKER_URL'],
        backend=None,
        include=['app.celery_config.celery_task']
    )
    celery_app.conf.update(app.config)

    return celery_app
