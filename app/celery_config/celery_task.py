import os
from app import celery_app
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_PASSWORD')
admin_email = os.environ.get('ADMIN_EMAIL')
sender_name = os.environ.get('SENDER_NAME')
print(os.environ.get('SENDER_NAME'))


@celery_app.task
def send_email(name, recipient, message):
    # Sender's email address and password

    print(str(message))
    # body = str(message)
    body = (f"Hi {name},\n\nThank you for visiting my website and reaching out to me. I appreciate your interest and "
            f"look forward to connecting with you.\n\nIf you have any specific questions or topics you'd like to "
            f"discuss, feel free to let me know. I'm here to help!\n\nBest regards,\nAkshay Rathod (DevDock)")

    # Recipient's email address
    recipient_email = recipient
    # Create the email message
    message = MIMEMultipart()
    # message["From"] = sender_email
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = recipient_email
    message["Subject"] = "Thanks for visiting My Page"

    # Attach body to the message
    message.attach(MIMEText(body, "plain"))

    # Connect to Gmail's SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Enable TLS
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Visitor notification sent successfully.")


@celery_app.task
def notify_admin(visitor_name, visitor_email, visitor_message):
    # Create the email message
    body = f"Hello Admin,\n\nA new visitor has interacted with the website:\n\nName: {visitor_name}\nEmail: {visitor_email}\nMessage: {visitor_message}\n\nPlease take appropriate action and respond accordingly.\n\nBest regards,\nDevDock"

    message = MIMEMultipart()

    # Set the sender and recipient
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = admin_email
    message["Subject"] = "New Visitor Notification"

    # Compose the body of the email

    # Attach body to the message
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Enable TLS
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, admin_email, message.as_string())

    print("Admin notification sent successfully.")


@celery_app.task
def celery_health_check():
    try:
        # Perform a simple operation to check the health
        # For example, you can check connectivity to a database, external service, etc.
        # If everything is fine, return a success message
        result = "Health check successful!"
        return {"success": True, "result": result}
    except Exception as e:
        # If there is an error, return a failure message
        return {"success": False, "error": str(e)}
