import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_welcome_mail(employee_email, name):
    try:
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        if not sender_email or not sender_password:
            raise ValueError("Email credentials not set in .env file.")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Welcome to the Team!"
        message["From"] = sender_email
        message["To"] = employee_email

        html_content = f"""
        <html>
            <body>
                <h2>Hello {name},</h2>
                <p>Welcome to the team! We are thrilled to have you join us.</p>
                <p>More details will follow shortly.</p>
                <p>Best regards,</p>
                <p>The HR Team</p>
            </body>
        </html>
        """
        part = MIMEText(html_content, "html")
        message.attach(part)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, employee_email, message.as_string())

        print(f"Welcome mail sent to {employee_email}")
        return True
    except Exception as e:
        print(f"Failed to send welcome mail: {e}")
        return False

def send_contract_mail(employee_email, name, end_date):
    try:
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Employment Contract"
        message["From"] = sender_email
        message["To"] = employee_email

        html_content = f"""
        <html>
            <body>
                <h2>Dear {name},</h2>
                <p>This email contains details regarding your employment contract with us.</p>
                <p>Your contract duration is until: <b>{end_date.strftime('%B %d, %Y')}</b></p>
                <p>Please find the full contract attached (this is a placeholder for now).</p>
                <p>Best regards,</p>
                <p>The HR Team</p>
            </body>
        </html>
        """
        part = MIMEText(html_content, "html")
        message.attach(part)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, employee_email, message.as_string())

        print(f"Contract mail sent to {employee_email}")
        return True
    except Exception as e:
        print(f"Failed to send contract mail: {e}")
        return False