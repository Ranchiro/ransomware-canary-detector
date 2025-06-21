# 🛡️ Ransomware Canary Detector

A Python-based early-warning **cybersecurity tool** that detects potential **ransomware attacks** by monitoring sensitive folders and watching for access or modification of **canary files**.

> 🚨 Get alerted the moment ransomware starts to strike.

---

## 📌 Features

- 🕵️‍♂️ Monitors sensitive directories in real time
- 🐦 Uses **canary files** as bait for ransomware
- 🔔 Sends instant alerts when suspicious activity is detected
- 📂 Configurable folder targets and alert rules via `config.yaml`
- 🧪 Includes unit tests for key modules
- 📜 Logs activity and potential threats

---

## 🖥️ How It Works

1. **Creates hidden canary files** in protected folders.
2. **Monitors file system activity** using a watchdog.
3. If a canary is **read, modified, or deleted**, the tool:
   - Triggers an **alert**
   - Logs the event
   - Optionally performs mitigation actions

---

## 🚀 Installation

```bash
git clone https://github.com/Ranchiro/ransomware-canary-detector.git
cd ransomware-canary-detector
pip install -r requirements.txt
