"""
Unit tests for privilege escalation monitor
"""
import unittest
from unittest.mock import Mock, patch
from src.alert_system import AlertSystem
from src.monitor import PrivilegeEscalationMonitor

class TestAlertSystem(unittest.TestCase):
    """Test cases for AlertSystem"""
    
    def setUp(self):
        self.alert_system = AlertSystem()
    
    def test_console_alert(self):
        """Test console alert generation"""
        event_data = {
            'timestamp': '2025-11-11T20:00:00',
            'type': 'Test Event',
            'user': 'testuser',
            'details': 'Test details'
        }
        
        # Should not raise exception
        self.alert_system.send_console_alert(event_data)
    
    def test_log_to_file(self):
        """Test secure file logging"""
        event_data = {
            'timestamp': '2025-11-11T20:00:00',
            'type': 'Test Event',
            'user': 'testuser',
            'details': 'Test details'
        }
        
        # Should not raise exception
        self.alert_system.log_to_secure_file(event_data)

class TestPrivilegeMonitor(unittest.TestCase):
    """Test cases for PrivilegeEscalationMonitor"""
    
    def setUp(self):
        self.monitor = PrivilegeEscalationMonitor()
    
    def test_initialization(self):
        """Test monitor initialization"""
        self.assertIsNotNone(self.monitor.alert_system)
        self.assertIsNotNone(self.monitor.os_type)
    
    def test_event_description(self):
        """Test event description retrieval"""
        desc = self.monitor._get_event_description(4672)
        self.assertIn("Special privileges", desc)

if __name__ == '__main__':
    unittest.main()
