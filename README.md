<div align="center">

# 🛡️ Ransomware Canary Detector

### Early-Warning Defense Against Ransomware Attacks

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-blue?style=for-the-badge)]()
[![Defense](https://img.shields.io/badge/Type-Defensive-success?style=for-the-badge)]()

<p align="center">
  <strong>A Python-based cybersecurity tool that detects ransomware attacks</strong><br/>
  By monitoring sensitive folders using canary files and alerting when they're compromised.
</p>

> 🚨 **Get alerted the moment ransomware starts to strike!**

---

</div>

## 🎯 How It Works

The detector uses a **canary file strategy** - a proven method in cybersecurity:

1. 📁 **Creates hidden canary files** in protected folders
2. 👁️ **Monitors them in real-time** for any changes
3. 🚨 **Alerts immediately** when ransomware accesses/modifies/deletes them
4. 📝 **Logs all activity** for forensic analysis

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📂 **Real-time Monitoring** | Watches sensitive directories continuously |
| 🦆 **Canary Files** | Uses decoy files as bait for ransomware |
| 🔔 **Instant Alerts** | Immediate notification on suspicious activity |
| ⚙️ **Configurable** | Customize folder targets via `config.yaml` |
| 🧪 **Unit Tested** | Includes tests for key modules |
| 📊 **Activity Logging** | Comprehensive threat logging |

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)
![Watchdog](https://img.shields.io/badge/Watchdog-4B8BBE?style=flat-square&logo=python&logoColor=white)

</div>

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Ranchiro/ransomware-canary-detector.git
cd ransomware-canary-detector

# Install dependencies
pip install -r requirements.txt

# Run the detector
python ransomware_canary_detector.py
```

### Configuration

Edit `config.yaml` to customize:
- Protected folder paths
- Alert methods
- Logging preferences

## 📁 Project Structure

```
ransomware-canary-detector/
├── ransomware_canary_detector.py  # Main script
├── config.yaml                     # Configuration
├── tests/                          # Unit tests
├── LICENSE                         # MIT License
└── README.md                       # Documentation
```

## 🛡️ Why Use Canary Detection?

- ⚡ **Faster than signature-based AV** - Detects zero-day ransomware
- 🎯 **Low false positives** - Only alerts on actual file tampering
- 💻 **Lightweight** - Minimal system resource usage
- 🔒 **Defense in depth** - Complements existing security tools

## 👨‍💻 Author

<div align="center">

**Ruchir Ganatra**

[![GitHub](https://img.shields.io/badge/GitHub-Ranchiro-181717?style=for-the-badge&logo=github)](https://github.com/Ranchiro)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ruchir-ganatra)

</div>

---

<div align="center">
  <sub>🛡️ Protect your data before it's too late!</sub>
</div>
