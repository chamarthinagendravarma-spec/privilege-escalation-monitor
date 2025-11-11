"""
Utility functions for the monitoring system
"""
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(log_file, log_level=logging.INFO):
    """
    Configure secure logging with rotation
    
    Args:
        log_file (Path): Path to log file
        log_level: Logging level (default: INFO)
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger('PrivilegeMonitor')
    logger.setLevel(log_level)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    # Create rotating file handler (max 10MB, keep 5 backups)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(log_level)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def sanitize_log_message(message):
    """
    Remove sensitive information from log messages
    
    Args:
        message (str): Original message
    
    Returns:
        str: Sanitized message
    """
    # Remove potential passwords, tokens, or sensitive data
    sensitive_keywords = ['password', 'token', 'secret', 'key', 'credential']
    
    for keyword in sensitive_keywords:
        if keyword.lower() in message.lower():
            # Mask the value after the keyword
            parts = message.split(keyword)
            if len(parts) > 1:
                message = parts[0] + keyword + ": [REDACTED]"
    
    return message

def format_event_details(event_data):
    """
    Format event data for logging and alerts
    
    Args:
        event_data (dict): Event information
    
    Returns:
        str: Formatted event details
    """
    timestamp = event_data.get('timestamp', datetime.now().isoformat())
    event_type = event_data.get('type', 'Unknown')
    user = event_data.get('user', 'Unknown')
    details = event_data.get('details', '')
    
    formatted = f"""
    ========== PRIVILEGE ESCALATION ALERT ==========
    Timestamp: {timestamp}
    Event Type: {event_type}
    User: {user}
    Details: {details}
    ================================================
    """
    
    return formatted
