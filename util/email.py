import smtplib
from email.message import EmailMessage
from util.config import *

def send_email(services_failed):
    config_info = get_config()
    message = EmailMessage()
    failed_services_message = "Failure detected on the following services: " + " ".join(services_failed)
    message.set_content(failed_services_message)
    message["Subject"] = "Network Service Failure Detected"
    message["From"] = config_info["sender_email"]
    message["To"] = config_info["receiver_email"]

    s = smtplib.SMTP_SSL(config_info["smtp_host"], config_info["smtp_port"])
    s.login(config_info["sender_email"], config_info["sender_pass"])
    s.send_message(message)
    s.quit()