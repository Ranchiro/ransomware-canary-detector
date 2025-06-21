# 🛠️ Installation Guide

## ✅ Requirements
- Python 3.8 or higher
- Works on Linux, Windows, macOS
- Packages: `watchdog`, `pyyaml`, `smtplib`

---

## 🐍 Virtual Environment Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## ⚙️ Configure `config.yaml`

Edit paths and canary file names based on your system.

```yaml
monitor_paths:
  - "/home/user/Documents/"
canary_files:
  - "canary.txt"
alert:
  method: email
  email_to: "you@example.com"
shutdown_on_alert: false
log_file: "./logs/activity.log"
```

---

## ▶️ Running the Tool

```bash
python main.py
```

Logs will be saved in `logs/activity.log`. Alerts will be triggered if any canary file is touched.

---

## 📧 Optional Email Alert Setup
Enable Gmail SMTP (use app password). Update config with:

```yaml
smtp:
  server: "smtp.gmail.com"
  port: 587
  username: "you@gmail.com"
  password: "your_app_password"
```

---

## 📍 Logs Location
Check `./logs/activity.log` for all monitored activity.

---

## 🛠 Troubleshooting
- 🟥 Error: FileNotFoundError → Check `monitor_paths` or `canary_files`
- 🟥 Email not sent? → Check SMTP setup and password
- 🟩 Logs not appearing? → Ensure `/logs/` folder exists

---

## 🖼️ Screenshot Placeholder
![Installation Screenshot](docs/screenshots/install.png)