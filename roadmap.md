# 🗺️ Project Roadmap

This file outlines the major milestones and planned improvements for **Ransomware Canary Detector** by **Ruchir Ganatra**.

---

## ✅ Version 1.0 — Initial Release (June 2025)

🎯 Core features delivered:
- ✅ Canary file monitoring across folders
- ✅ Real-time alerts (Log, Email, Optional Shutdown)
- ✅ YAML configuration (`config.yaml`)
- ✅ Logging system (`logs/activity.log`)
- ✅ Modular Python codebase (`/src`)
- ✅ Full documentation (`/docs`)

---

## 🔄 Version 2.0 — Advanced Alerting (Planned: August 2025)

🎯 Features in development:
- 🧩 Webhook support (Slack, Discord, Microsoft Teams)
- 💻 Local GUI interface (Tkinter-based control panel)
- 📄 Config schema validation with `cerberus` or `voluptuous`
- 🧪 Built-in ransomware simulator for test mode
- 🖥️ Windows tray icon + Linux background daemon mode
- 📡 API integration to send alerts to external services (e.g., PagerDuty)

---

## 🌐 Version 3.0 — Enterprise Readiness (Planned: November 2025)

🎯 Big picture upgrades:
- 🧠 Live threat intelligence feed from public sources (e.g., URLhaus, MISP)
- 🛡️ File integrity verification using SHA-256 hash comparison
- 🧩 Syslog and SIEM (Security Information and Event Management) compatibility
- 🪟 Integration with Windows Defender API (via PowerShell or WMI)
- 🐧 Linux: Integrate with ClamAV to scan suspicious changes
- 🧭 Role-based alerts (email SOC analyst, escalate to admin, etc.)
- 📦 Docker container support

---

## 📅 Suggested Release Timeline

| Version  | Release Window   | Notes                             |
|----------|------------------|-----------------------------------|
| `1.0.0`  | ✅ June 2025     | Stable release                    |
| `2.0.0`  | August 2025      | Alerting + GUI                    |
| `3.0.0`  | November 2025    | Enterprise security features      |

---

## 🧑‍💻 Author

Created and maintained by [**Ruchir Ganatra**](https://github.com/Ranchiro)  
📖 Medium: [ruchirganatra.medium.com](https://ruchirganatra.medium.com)  
🌐 Linktree: [linktr.ee/ruchir.ganatra](https://linktr.ee/ruchir.ganatra)

---

Feel free to contribute ideas! Open a new issue or discussion on GitHub to propose a new feature.
