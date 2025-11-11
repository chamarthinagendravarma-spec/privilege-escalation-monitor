"""
Configuration module for Privilege Escalation Monitor
Loads settings from environment variables for security
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'privilege_events.log'

# Create logs directory if it doesn't exist
LOG_DIR.mkdir(exist_ok=True)

# Email configuration
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

# Alert settings
ALERT_THRESHOLD = int(os.getenv('ALERT_THRESHOLD', 3))
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', 60))

# Windows Event IDs to monitor
WINDOWS_EVENT_IDS = [
    4672,  # Special privileges assigned
    4673,  # Privileged service called
    4688,  # Process creation
    4697,  # Service installed
    4698,  # Scheduled task created
    4732,  # Member added to security group
]

# Validation
if not SENDER_EMAIL or not SENDER_PASSWORD:
    print("WARNING: Email credentials not configured in .env file")
