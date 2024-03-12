import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import datetime

from email_template import EmailTempalte
from config import Config


def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(to_email, otp, expiration):
    # Email configuration
    from_email = Config.SENDER_EMAILL
    password = Config.SENDER_PASSWORD
    smtp_server = Config.SMTP_SERVER
    smtp_port = Config.SMTP_PORT
    
    print("Email Validation data = ", from_email, password, smtp_server, smtp_port)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = 'OTP Verification'

    # Read the HTML template
    html_template = EmailTempalte.TEMPLATE

    # Replace the OTP placeholder in the HTML template
    html_content = html_template.replace('{{ otp }}', otp)
    html_content = html_content.replace('{{ expiration }}', expiration.strftime('%Y-%m-%d %H:%M:%S'))

    # Attach the HTML content to the email message
    message.attach(MIMEText(html_content, 'html'))

    # Send the email using SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(message)


def main():
    
    # Generate OTP
    otp = generate_otp()
    
    # Set the expiration time (e.g., 5 minutes from now)
    expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=5)

    # Send the OTP email
    to_email = Config.TO_EMAIL
    send_otp_email(to_email, otp, expiration_time)

if __name__ == "__main__":
    main()