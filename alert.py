# Alert mechanisms: shutdown, email
import smtplib
import os
import platform
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import yaml

# Load config
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def send_email_alert(subject, body):
    try:
        email_config = config.get('email', {})
        sender_email = email_config['from']
        receiver_email = email_config['to']
        password = email_config['password']
        smtp_server = email_config.get('smtp_server', 'smtp.gmail.com')
        smtp_port = email_config.get('smtp_port', 587)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        logger.info("✅ Email alert sent to %s", receiver_email)
    except Exception as e:
        logger.error("❌ Failed to send email alert: %s", str(e))

def shutdown_system():
    try:
        logger.warning("⚠️ Triggering system shutdown...")
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /s /t 1")
        elif system == "Linux" or system == "Darwin":
            os.system("shutdown now")
        else:
            logger.error("Unsupported OS for shutdown.")
    except Exception as e:
        logger.error("❌ Failed to shutdown system: %s", str(e))

def trigger_alert(message):
    logger.warning("🚨 ALERT: %s", message)
    
    if "email" in config.get("alerts", []):
        send_email_alert("🚨 Ransomware Canary Triggered", message)

    if "shutdown" in config.get("alerts", []):
        shutdown_system()
