# 🛡️ Ransomware Canary Detector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Beta-yellow)

A high-level defensive cybersecurity tool that monitors **canary files** placed in sensitive directories to detect early signs of ransomware activity.

---

## 📊 Visual Overview (Diagram Placeholder)
```
+-----------------+
|  config.yaml    |
+--------+--------+
         |
         v
+--------+--------+
|  Canary Monitor |
+--------+--------+
         |
         v
+--------+--------+
|  Alert Engine   |--> Email / Log / Shutdown
+-----------------+
```

---

## ✅ Features
- Canary file monitoring
- Real-time event logging
- Email/shutdown alert system
- YAML-based configuration
- Lightweight and easy to deploy

## 🎯 Use Cases
- Students & Learners
- SOC Analysts & Blue Teamers
- Malware Researchers
- Personal or Enterprise use

## 🖼️ Demo Screenshot (Placeholder)
![Demo](docs/demo.png)

---

## ⚙️ Installation

```bash
git clone https://github.com/Ranchiro/ransomware-canary-detector.git
cd ransomware-canary-detector
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🧩 Configuration
Edit the `config.yaml` file as needed.

### Example `config.yaml`:
```yaml
monitor_paths:
  - "/home/user/Documents/"
  - "C:/Users/YourName/Desktop/"

canary_files:
  - "canary1.txt"
  - "canary2.docx"

alert:
  method: email
  email_to: "you@example.com"

shutdown_on_alert: false
log_file: "./logs/activity.log"
```

## 🚀 Usage

```bash
python main.py
```

## 📤 Output
- Logs every event in `/logs/activity.log`
- Email/shutdown triggered upon canary file interaction

---

## 👨‍💻 Author
**Ruchir Ganatra**  
- 🌐 [Linktree](https://linktr.ee/ruchir.ganatra)
- ✍️ [Medium](https://ruchirganatra.medium.com)
- 💻 [GitHub](https://github.com/Ranchiro)

## 📜 License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 🙏 Credits
- Python community for `watchdog`, `pyyaml`
- Open-source inspiration from Sysmon & Blue Teams