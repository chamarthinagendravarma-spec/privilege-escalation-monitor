"""
Alert system for sending notifications via email and console
"""
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from src import config
from src.utils import setup_logger, format_event_details

logger = setup_logger(config.LOG_FILE)

class AlertSystem:
    """Handles alert notifications for privilege escalation events"""
    
    def __init__(self):
        self.smtp_server = config.SMTP_SERVER
        self.smtp_port = config.SMTP_PORT
        self.sender_email = config.SENDER_EMAIL
        self.sender_password = config.SENDER_PASSWORD
        self.recipient_email = config.RECIPIENT_EMAIL
        
    def send_email_alert(self, event_data):
        """
        Send email alert for privilege escalation event
        
        Args:
            event_data (dict): Event information
        
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        if not self.sender_email or not self.sender_password:
            logger.warning("Email credentials not configured. Skipping email alert.")
            return False
        
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = f"🚨 SECURITY ALERT: Privilege Escalation Detected"
            message["From"] = self.sender_email
            message["To"] = self.recipient_email
            
            # Create plain text and HTML versions
            text_content = format_event_details(event_data)
            
            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif;">
                    <div style="background-color: #ff0000; color: white; padding: 20px;">
                        <h2>🚨 SECURITY ALERT: Privilege Escalation Detected</h2>
                    </div>
                    <div style="padding: 20px; background-color: #f9f9f9;">
                        <p><strong>Timestamp:</strong> {event_data.get('timestamp', 'N/A')}</p>
                        <p><strong>Event Type:</strong> {event_data.get('type', 'Unknown')}</p>
                        <p><strong>User:</strong> {event_data.get('user', 'Unknown')}</p>
                        <p><strong>Details:</strong> {event_data.get('details', 'No details available')}</p>
                    </div>
                    <div style="padding: 20px; background-color: #fff3cd;">
                        <p><strong>Action Required:</strong> Investigate this event immediately and verify if this was an authorized action.</p>
                    </div>
                </body>
            </html>
            """
            
            # Attach parts
            part1 = MIMEText(text_content, "plain")
            part2 = MIMEText(html_content, "html")
            message.attach(part1)
            message.attach(part2)
            
            # Create secure SSL context
            context = ssl.create_default_context()
            
            # Send email using STARTTLS
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Email alert sent successfully to {self.recipient_email}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email alert: {str(e)}")
            return False
    
    def send_console_alert(self, event_data):
        """
        Display alert on console
        
        Args:
            event_data (dict): Event information
        """
        alert_message = format_event_details(event_data)
        print("\n" + "="*50)
        print("🚨 PRIVILEGE ESCALATION ALERT 🚨")
        print(alert_message)
        print("="*50 + "\n")
        logger.warning(f"Console alert displayed for event: {event_data.get('type', 'Unknown')}")
    
    def log_to_secure_file(self, event_data):
        """
        Log event to secure file with restricted permissions
        
        Args:
            event_data (dict): Event information
        """
        try:
            log_entry = f"{datetime.now().isoformat()} | " \
                       f"Type: {event_data.get('type', 'Unknown')} | " \
                       f"User: {event_data.get('user', 'Unknown')} | " \
                       f"Details: {event_data.get('details', 'N/A')}\n"
            
            logger.critical(log_entry.strip())
            
        except Exception as e:
            logger.error(f"Failed to write to secure log file: {str(e)}")
    
    def trigger_alert(self, event_data):
        """
        Trigger all alert mechanisms
        
        Args:
            event_data (dict): Event information
        """
        self.send_console_alert(event_data)
        self.log_to_secure_file(event_data)
        self.send_email_alert(event_data)
