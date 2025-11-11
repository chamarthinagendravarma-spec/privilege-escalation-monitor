"""
Main privilege escalation monitoring system
Monitors Windows Event Logs and Linux system logs for unauthorized privilege changes
"""
import sys
import time
import platform
from datetime import datetime
from src import config
from src.alert_system import AlertSystem
from src.utils import setup_logger

logger = setup_logger(config.LOG_FILE)

class PrivilegeEscalationMonitor:
    """Main monitoring class for detecting privilege escalation attempts"""
    
    def __init__(self):
        self.alert_system = AlertSystem()
        self.os_type = platform.system()
        self.last_check_time = datetime.now()
        self.event_count = {}
        
        logger.info(f"Privilege Escalation Monitor initialized on {self.os_type}")
    
    def monitor_windows_events(self):
        """
        Monitor Windows Event Logs for privilege escalation indicators
        """
        if self.os_type != "Windows":
            logger.warning("Not running on Windows. Skipping Windows event monitoring.")
            return
        
        try:
            import win32evtlog
            import win32evtlogutil
            import win32con
            
            server = 'localhost'
            logtype = 'Security'
            
            # Open event log
            hand = win32evtlog.OpenEventLog(server, logtype)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
            
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            
            for event in events:
                # Check if event is one of our monitored Event IDs
                if event.EventID in config.WINDOWS_EVENT_IDS:
                    
                    # Extract event details
                    event_data = {
                        'timestamp': event.TimeGenerated.isoformat(),
                        'type': f'Windows Event ID {event.EventID}',
                        'user': event.StringInserts[0] if event.StringInserts else 'Unknown',
                        'details': self._get_event_description(event.EventID)
                    }
                    
                    # Track event frequency
                    event_key = f"{event.EventID}_{event_data['user']}"
                    self.event_count[event_key] = self.event_count.get(event_key, 0) + 1
                    
                    # Trigger alert if threshold exceeded
                    if self.event_count[event_key] >= config.ALERT_THRESHOLD:
                        logger.critical(f"Privilege escalation detected: Event ID {event.EventID}")
                        self.alert_system.trigger_alert(event_data)
                        self.event_count[event_key] = 0  # Reset counter
            
            win32evtlog.CloseEventLog(hand)
            
        except ImportError:
            logger.error("pywin32 not installed. Install with: pip install pywin32")
        except Exception as e:
            logger.error(f"Error monitoring Windows events: {str(e)}")
    
    def monitor_linux_logs(self):
        """
        Monitor Linux auth logs for privilege escalation indicators
        """
        if self.os_type != "Linux":
            logger.warning("Not running on Linux. Skipping Linux log monitoring.")
            return
        
        try:
            import subprocess
            
            # Common privilege escalation indicators in Linux logs
            suspicious_patterns = [
                'sudo',
                'su -',
                'COMMAND',
                'authentication failure',
                'FAILED su',
                'session opened for user root'
            ]
            
            # Read auth.log or secure log
            log_files = ['/var/log/auth.log', '/var/log/secure']
            
            for log_file in log_files:
                try:
                    # Use tail to get recent entries
                    result = subprocess.run(
                        ['sudo', 'tail', '-n', '100', log_file],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    
                    if result.returncode == 0:
                        lines = result.stdout.split('\n')
                        
                        for line in lines:
                            # Check for suspicious patterns
                            for pattern in suspicious_patterns:
                                if pattern in line:
                                    
                                    event_data = {
                                        'timestamp': datetime.now().isoformat(),
                                        'type': 'Linux Authentication Event',
                                        'user': self._extract_user_from_log(line),
                                        'details': line[:200]  # First 200 chars
                                    }
                                    
                                    # Track frequency
                                    event_key = f"{pattern}_{event_data['user']}"
                                    self.event_count[event_key] = self.event_count.get(event_key, 0) + 1
                                    
                                    if self.event_count[event_key] >= config.ALERT_THRESHOLD:
                                        logger.critical(f"Privilege escalation detected in {log_file}")
                                        self.alert_system.trigger_alert(event_data)
                                        self.event_count[event_key] = 0
                    
                except FileNotFoundError:
                    continue
                except subprocess.TimeoutExpired:
                    logger.warning(f"Timeout reading {log_file}")
                    continue
            
        except Exception as e:
            logger.error(f"Error monitoring Linux logs: {str(e)}")
    
    def _get_event_description(self, event_id):
        """Get human-readable description for Windows Event IDs"""
        descriptions = {
            4672: "Special privileges assigned to new logon",
            4673: "A privileged service was called",
            4688: "A new process has been created",
            4697: "A service was installed on the system",
            4698: "A scheduled task was created",
            4732: "A member was added to a security-enabled local group"
        }
        return descriptions.get(event_id, "Unknown event type")
    
    def _extract_user_from_log(self, log_line):
        """Extract username from log line"""
        # Simple extraction - can be enhanced
        if 'user=' in log_line:
            parts = log_line.split('user=')
            if len(parts) > 1:
                return parts[1].split()[0]
        return "Unknown"
    
    def start_monitoring(self):
        """Start continuous monitoring loop"""
        logger.info("Starting privilege escalation monitoring...")
        print(f"\n{'='*60}")
        print("🔒 Privilege Escalation Monitor Started")
        print(f"{'='*60}")
        print(f"Operating System: {self.os_type}")
        print(f"Check Interval: {config.CHECK_INTERVAL} seconds")
        print(f"Log File: {config.LOG_FILE}")
        print(f"{'='*60}\n")
        
        try:
            while True:
                # Monitor based on OS type
                if self.os_type == "Windows":
                    self.monitor_windows_events()
                elif self.os_type == "Linux":
                    self.monitor_linux_logs()
                else:
                    logger.warning(f"Unsupported OS: {self.os_type}")
                
                # Wait before next check
                time.sleep(config.CHECK_INTERVAL)
                
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
            print("\n\n🛑 Monitoring stopped. Goodbye!")
        except Exception as e:
            logger.critical(f"Critical error in monitoring loop: {str(e)}")
            raise

def main():
    """Main entry point"""
    monitor = PrivilegeEscalationMonitor()
    monitor.start_monitoring()

if __name__ == "__main__":
    main()
