from flask import Flask, Blueprint, make_response, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_mail import Mail
from flask_cors import CORS
import os
from celery import Celery
from app.celery_config.celery_worker import make_celery

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes
api = Api(app)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
print(os.environ.get('CELERY_BROKER'))
app.config['CELERY_BROKER_URL'] = os.environ.get('CELERY_BROKER')
print("RabbitMQ URI:", app.config['CELERY_BROKER_URL'])
app.config['BROKER_URL'] = os.environ.get('CELERY_BROKER')

mongo = PyMongo(app)
mail = Mail(app)
celery_app = make_celery(app)
