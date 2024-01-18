from flask import Flask, Blueprint, make_response, jsonify, render_template, request
from flask_restful import Resource, Api
from app import api, app, mail
from flask_mail import Mail, Message
from app.master.controller import add_form
# from app.utils.common import send_email
from app.celery_config.celery_task import send_email, notify_admin, celery_health_check
import os

app_bp = Blueprint('app_bp', __name__)


class SubmitForm(Resource):
    def post(self):
        print(os.environ.get('CELERY_BROKER'))
        try:
            if request.is_json:
                # Handle JSON data
                data = request.get_json(force=True)
                name = data.get('Name')
                email = data.get('Email')
                message = data.get('Message')
                print(f"Received JSON data: Name={name}, Email={email}, Message={message}")
            else:
                # Handle form data
                name = request.form.get('Name')
                email = request.form.get('Email')
                message = request.form.get('Message')
                print(f"Received form data: Name={name}, Email={email}, Message={message}")

            # Process the data
            process_data = add_form(name, email, message)
            send_alert = send_email.delay(name, email, message)
            admin_alert = notify_admin.delay(name, email, message)

            print("Form processed successfully")

            return jsonify({'success': True, 'message': 'Form submitted successfully!'})

        except Exception as e:
            print(f"Error processing form: {str(e)}")
            return jsonify({'success': False, 'message': 'An error occurred. Please try again.'})


class FlaskHealthCheck(Resource):
    def get(self):
        return make_response(jsonify({"health-check": "true"}), 200)


class TestEndPoint(Resource):

    def get(self):
        return make_response(jsonify({"Modified Version": "v1"}), 200)


# class CeleryHealthCheck(Resource):
#     def get(self):
#         try:
#             # Trigger the Celery health check task
#             result = celery_health_check.apply_async().get()
#             if result["success"]:
#                 return {"status": "ok", "message": result["message"]}, 200
#             else:
#                 return {"status": "error", "message": result["message"]}, 500
#         except Exception as e:
#             return {"status": "error", "message": str(e)}, 500

class SenderIP(Resource):

    def get(self):
        forwarded_for = request.headers.get('X-Forwarded-For', None)
        print(forwarded_for)
        print(type(forwarded_for))
        ip_address = request.remote_addr
        resp = {"sender ip": str(forwarded_for)}
        return make_response(resp)


api.add_resource(FlaskHealthCheck, "/health-check")
api.add_resource(TestEndPoint, "/test")
# api.add_resource(CeleryHealthCheck, "/celery-health-check")
api.add_resource(SubmitForm, "/submit_form")
api.add_resource(SenderIP, "/sender-ip")
