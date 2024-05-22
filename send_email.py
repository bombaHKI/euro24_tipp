import json
import os
import smtplib # Import smtplib for the actual sending function
from email.mime.text import MIMEText # Import the email modules we'll need
from email.mime.multipart import MIMEMultipart

# Email account credentials
# Email account credentials
sender_json_path = os.path.join(os.path.dirname(__file__), 'data/email_user_info.json')
with open(sender_json_path, 'r', encoding='utf-8') as f:
    senderJson = json.load(f)
sender_email = senderJson["address"]
password = senderJson["app-password"]

def send_email(receiver_email, receiver_name, message_file_name):
    message_path = os.path.join(os.path.dirname(__file__),
                                'messages/{name}.json'.format(name=message_file_name))
    with open(message_path, 'r', encoding='utf-8') as f:
        messageJson = json.load(f)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = messageJson["subject"]
    msg.attach(MIMEText(messageJson["body"].format(name = receiver_name), 'plain'))

    # Set up the SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully using Gmail SMTP server')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

#send_email("kada626@gmail.com", "Haála Kada", "at_signup")
