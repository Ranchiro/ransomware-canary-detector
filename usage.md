# 🚀 Usage Guide

## ▶️ Starting the App

```bash
python main.py
```

---

## 🔐 Simulating Ransomware Test

1. Create `canary.txt` in a monitored path
2. Modify/delete it manually or via a script
3. Watch for logs or alert

---

## 📁 Canary File Placement
Example canary file structure:

```
/Documents/
├── report.docx
├── canary.txt 👈
```

---

## 🛎️ Real-Time Alert Logging

When an event is detected, logs like:

```
[INFO] Modified: /home/user/Documents/canary.txt at 2025-06-21 15:42
[ALERT] Triggered by: canary.txt
```

---

## 📧 Email/Webhook Alert Config

In `config.yaml`:

```yaml
alert:
  method: email
  email_to: "alert@example.com"
```

---

## 🛡️ Defensive Response Options

- Shutdown system:
```yaml
shutdown_on_alert: true
```
- Email only (safe mode): set shutdown to false

---

## ❌ Exit and Debug Mode

- Press `Ctrl+C` to exit safely
- Use `logging.debug()` for verbose output

---

## 🧠 Common Issues & Fixes

| Problem | Fix |
|--------|------|
| Alert not triggered | Check file names in config |
| Email not received | Use app password, correct SMTP |
| No logs | Ensure `logs/` folder exists |

---

## 💡 Pro Tips

- Place canary files that match ransomware patterns (e.g. `.docx`, `.xls`)
- Use virtual machines to simulate ransomware behavior