# 🧪 Test Plan for Ransomware Canary Detector

## 🎯 Purpose and Scope
To validate that the tool reliably detects modifications to canary files, triggers appropriate alerts, and logs activity.

---

## ✅ Functional Test Cases

| TC ID   | Description                          | Input             | Expected Output                         |
|---------|--------------------------------------|-------------------|------------------------------------------|
| TC-01   | Modify canary file                   | edit canary1.txt  | Alert triggered, log updated             |
| TC-02   | Delete canary file                   | rm canary2.docx   | Alert triggered, log + shutdown/email    |
| TC-03   | Rename canary file                   | mv canary.txt abc.txt | Alert triggered                       |
| TC-04   | Modify non-canary file               | edit notes.txt    | No alert                                 |
| TC-05   | Invalid path in config               | bad path config   | Error shown, log entry                   |
| TC-06   | Email alert sends correctly          | SMTP config       | Email received                           |
| TC-07   | Logs saved correctly                 | activity events   | Entries in logs/activity.log             |
| TC-08   | Shutdown triggered                   | config: true      | System initiates shutdown                |
| TC-09   | Load valid config                    | config.yaml       | Monitor starts correctly                 |
| TC-10   | Multiple paths/canary files          | 2 paths + 3 files | All monitored properly                   |

---

## 🧪 Manual Test Procedure
1. Start tool: `python main.py`
2. Modify, delete, or rename a test canary file
3. Observe log file and alerts

---

## 🛠 Tools Required
- Python 3.8+
- VS Code / Terminal
- SMTP-capable email account (optional)

---

## 🤖 Automation Plan
- Use `pytest`
- Use `unittest.mock` to simulate file events and SMTP
- GitHub Actions for CI

---

## 🧯 Failure Handling
- If config fails, tool exits with error log
- If log file is not accessible, fallback to console output

---

## ✅ Success Criteria
- Canary events are caught instantly
- Alerts are issued based on settings
- All paths and formats in config are parsed

---

## 👨‍💻 Author
Ruchir Ganatra  
[GitHub](https://github.com/Ranchiro)