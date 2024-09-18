import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import configparser
import os

def read_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    config.read(file_path)
    return config['EmailConfiguration']

def send_email(subject, body, to_email, attachment_path, sender_email, sender_password, smtp_server, smtp_port):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the CV as an attachment
    with open(attachment_path, 'rb') as f:
        attachment = MIMEApplication(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
        message.attach(attachment)

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")
        raise

if __name__ == "__main__":
    # This section is for testing purposes only
    try:
        # Read email configuration from the config file
        email_config = read_config()

        # Test sending an email
        subject = "Test Subject"
        body = "This is a test email."
        cv_path = "path/to/your/CV.pdf"
        recipient_email = "recipient@example.com"

        send_email(subject, body, recipient_email, cv_path,
                   email_config['sender_email'], email_config['sender_password'],
                   email_config['smtp_server'], int(email_config['smtp_port']))

        print("Test email sent successfully.")
    except Exception as e:
        print(f"Error during test: {e}")