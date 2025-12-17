# Privilege Escalation Monitoring System

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blueviolet)](https://github.com/chamarthinagendravarma-spec/privilege-escalation-monitor)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/chamarthinagendravarma-spec/privilege-escalation-monitor)

**Real-time Security Monitoring & Privilege Escalation Detection**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [Contributing](#-contributing)

</div>

---

## 📋 About

An intelligent, automated security monitoring system that detects unauthorized privilege escalation attempts in real-time and alerts administrators through multiple channels. Protect your infrastructure from unauthorized privilege escalations with comprehensive cross-platform monitoring.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Real-time Monitoring** | Continuously monitors system event logs for suspicious activities |
| 🚨 **Multi-Channel Alerts** | Email, console, and secure file logging notifications |
| 🖥️ **Cross-Platform Support** | Seamlessly works on Windows and Linux systems |
| 🔒 **Secure Logging** | Encrypted storage with automatic log rotation |
| ⚙️ **Highly Configurable** | Simple environment variable-based configuration |
| 📊 **Event Tracking** | Detailed logging of 6+ Windows Event IDs and Linux indicators |
| 🛡️ **Security First** | Built with security best practices in mind |

---

## 🔧 System Requirements

```
✓ Python 3.8 or higher
✓ Windows 10/11 OR Linux (Ubuntu 20.04+, CentOS 8+)
✓ Administrative/root privileges for log access
✓ SMTP server access for email alerts (optional)
```

---

## 🚀 Quick Start

### Option 1: Windows
```bash
# Clone the repository
git clone https://github.com/chamarthinagendravarma-spec/privilege-escalation-monitor.git
cd privilege-escalation-monitor

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure your settings
copy .env.example .env
# Edit .env with your configuration

# Run as Administrator
python -m src.monitor
```

### Option 2: Linux
```bash
# Clone the repository
git clone https://github.com/chamarthinagendravarma-spec/privilege-escalation-monitor.git
cd privilege-escalation-monitor

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure your settings
cp .env.example .env
# Edit .env with your configuration

# Run with sudo privileges
sudo -E python -m src.monitor
```

---

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

```bash
# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
RECIPIENT_EMAIL=admin@company.com

# Monitoring Configuration
CHECK_INTERVAL=60                    # Check interval in seconds
LOG_LEVEL=INFO                       # DEBUG, INFO, WARNING, ERROR
ENABLE_ENCRYPTION=true               # Enable log encryption
```

> **💡 Pro Tip:** Use [Gmail App Passwords](https://support.google.com/accounts/answer/185833) for email configuration instead of your main password.

---

## 📖 Usage

### Windows (Administrator Command Prompt)
```bash
venv\Scripts\activate
python -m src.monitor
```

### Linux (Terminal with sudo)
```bash
source venv/bin/activate
sudo -E python -m src.monitor
```

### Run Tests
```bash
python -m unittest tests.test_monitor
```

---

## 👀 Monitored Events

### Windows Event IDs

| Event ID | Description |
|----------|-------------|
| **4672** | Special privileges assigned to a new logon |
| **4673** | A privileged service was called |
| **4688** | A new process has been created |
| **4697** | A service was installed in the system |
| **4698** | A scheduled task was created |
| **4732** | A member was added to a security-enabled local group |

### Linux Indicators

| Indicator | Description |
|-----------|-------------|
| 🔐 Sudo command execution | Privilege escalation attempts |
| 🔄 Su (switch user) attempts | User switching activities |
| ⚠️ Authentication failures | Failed authentication attempts |
| 👤 Root session activities | Root user session logs |

---

## 🧪 Testing

Run comprehensive unit tests:

```bash
python -m unittest tests.test_monitor -v
```

---

## 🔐 Security Considerations

> ⚠️ **Important Security Notes:**

- ❌ **Never** commit `.env` file to version control
- 🔑 Use app-specific passwords for email authentication
- 📋 Regularly review logs in the `logs/` directory
- 👤 Run with minimum required privileges
- 🔄 Keep dependencies updated: `pip install --upgrade -r requirements.txt`
- 🛡️ Run in isolated environments or containers for production
- 📊 Monitor system resource usage during continuous monitoring

---

## 📁 Project Structure

```
privilege-escalation-monitor/
├── src/
│   ├── monitor.py          # Main monitoring engine
│   ├── alerting.py         # Alert handlers
│   └── utils.py            # Utility functions
├── tests/
│   └── test_monitor.py     # Unit tests
├── logs/                   # Log files (created at runtime)
├── .env.example            # Configuration template
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md              # This file
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

For major changes, please open an issue first to discuss the proposed changes.

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Nagendra Varma

Permission is hereby granted, free of charge...
```

---

## 👨‍💻 Author

**Nagendra Varma**
- 📧 Email: your-email@example.com
- 🐙 GitHub: [@chamarthinagendravarma-spec](https://github.com/chamarthinagendravarma-spec)
- 💼 LinkedIn: [Your LinkedIn Profile]

---

## 📞 Support & Issues

Found a bug or have a suggestion? [Open an Issue](https://github.com/chamarthinagendravarma-spec/privilege-escalation-monitor/issues) and let us know!

---

<div align="center">

**[⬆ back to top](#privilege-escalation-monitoring-system)**

Made with ❤️ by [Nagendra Varma](https://github.com/chamarthinagendravarma-spec)

</div>