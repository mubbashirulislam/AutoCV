import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import configparser

def read_config(file_path='config.ini'):
    config = configparser.ConfigParser()
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
        attachment.add_header('Content-Disposition', 'attachment', filename='Your_CV.pdf')
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

if __name__ == "__main__":
    # Read email configuration from the config file
    email_config = read_config()

    # Leave subject and body empty for customization
    subject = ""
    body = ""

    # Specify the path to your CV
    cv_path = "path/to/your/CV.pdf"

    # Specify the list of recipient email addresses
    recipient_emails = ["recipient@example.com"]

    # Loop through the list of recipients and send the email
    for recipient_email in recipient_emails:
        send_email(subject, body, recipient_email, cv_path,
                   email_config['sender_email'], email_config['sender_password'],
                   email_config['smtp_server'], int(email_config['smtp_port']))

    print("Emails sent successfully.")
