# 🧠 Architecture Overview

## 🔧 Technical Overview
The **Ransomware Canary Detector** is a Python-based real-time monitoring tool that watches specific directories and designated *canary files*. If these files are accessed, modified, or deleted, it assumes possible ransomware activity and triggers an alert (email, log, or system shutdown).

---

## 🧩 Modules Used
- `watchdog`: For file system event monitoring
- `pyyaml`: For config file parsing
- `smtplib` / `email`: For sending alerts via email (optional)
- `os`, `sys`, `logging`, `threading`: Core functionality

---

## 📁 Folder Structure
```
/src
  └── watcher.py
  └── alert.py
  └── config_loader.py
/logs
  └── activity.log
/test
  └── test_config.py
  └── test_alerts.py
config.yaml
main.py
docs/
```

---

## 🔄 Flow Diagram (Text Representation)
```
+------------+
| config.yaml|
+-----+------+
      |
      v
+-----+------+     Event?     +-------------+
| config_loader|------------->| watcher.py  |
+------------+               +------+-------+
                                     |
                            +--------v--------+
                            |   alert.py      |
                            +--------+--------+
                                     |
                        +------------v----------+
                        |  email / log / shutdown |
                        +------------------------+
```

---

## 🎯 Canary Trigger Logic
- Uses `watchdog.observers.Observer` with `FileSystemEventHandler`
- Listens to `on_modified`, `on_deleted`, and `on_moved` events
- If event.path matches a canary file: trigger alert

---

## 📜 Logging Architecture
- Logging to `logs/activity.log`
- Log level: `INFO` (configurable)
- Optional email logging or console output

---

## 🚨 Alert System
- Alert methods:
  - Email (via SMTP)
  - System Shutdown (Windows/Linux)
  - Console or File log

---

## 🧱 Tech Stack
- Python 3.8+
- `watchdog`, `pyyaml`, `smtplib`
- Tested on Linux & Windows 10

---

## 🛠️ Future Enhancements
- Webhook support (Slack, Discord)
- GUI Dashboard (Tkinter or Flask)
- Agent + Server model
- Threat feed enrichment
- File integrity hash detection

---

## 🗒 Developer Notes
- Use test_canary.txt files for safe testing
- Do not place real sensitive files in monitored list
- Email alerts need secure SMTP setup (Gmail App Passwords etc.)

---