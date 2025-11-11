# Privilege Escalation Monitoring System

An automated security monitoring system that detects unauthorized privilege escalation attempts in real-time and alerts administrators.

## Features

- 🔍 **Real-time Monitoring**: Continuously monitors system event logs
- 🚨 **Multi-Channel Alerts**: Email, console, and secure file logging
- 🖥️ **Cross-Platform**: Supports both Windows and Linux systems
- 🔒 **Secure Logging**: Encrypted storage with log rotation
- ⚙️ **Configurable**: Easy configuration through environment variables

## System Requirements

- Python 3.8 or higher
- Windows 10/11 or Linux (Ubuntu 20.04+, CentOS 8+)
- Administrative/root privileges for log access
- SMTP server access for email alerts (optional)

## Installation

1. Clone this repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and configure your settings

## Configuration

Edit the `.env` file with your settings:

SMTP_SERVER=smtp.gmail.com <br>
SMTP_PORT=587 <br>
SENDER_EMAIL=your-email@gmail.com <br>
SENDER_PASSWORD=your-app-password <br>
RECIPIENT_EMAIL=admin@company.com <br>
CHECK_INTERVAL=60 <br>

## Usage

### Windows
Run Command Prompt as Administrator:
<br>
venv\Scripts\activate
<br>
python -m src.monitor

### Linux
Run with sudo privileges:
<br>
source venv/bin/activate
<br>
sudo -E python -m src.monitor

## Monitored Events

### Windows Event IDs
- 4672: Special privileges assigned
- 4673: Privileged service called
- 4688: Process creation
- 4697: Service installed
- 4698: Scheduled task created
- 4732: Security group membership change

### Linux Indicators
- Sudo command execution
- Su (switch user) attempts
- Authentication failures
- Root session activities

## Testing

Run unit tests:
python -m unittest tests.test_monitor

## Security Considerations

- Never commit `.env` file to version control
- Use app-specific passwords for email
- Regularly review logs in `logs/` directory
- Run with minimum required privileges
- Keep dependencies updated

## License

MIT License

## Author

Nagendra Varma

## Contributing

Pull requests are welcome. For major changes, please open an issue first.
