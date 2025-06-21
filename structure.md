# 🗂️ Folder Structure

This document outlines the folder and file structure of the **Ransomware Canary Detector** project by **Ruchir Ganatra**.

---

## 📁 Directory Tree

ransomware-canary-detector/
├── main.py # Entry point of the application
├── config.yaml # User-editable configuration file
├── requirements.txt # Python dependencies
│
├── /src # Core source code modules
│ ├── monitor.py # Watches directories for changes
│ ├── detector.py # Contains canary file detection logic
│ └── alert.py # Handles alert actions (email/shutdown)
│
├── /logs # Runtime log storage
│ └── activity.log # Log file with timestamps and events
│
├── /test # Unit and functional tests
│ ├── test_config.py # Tests for configuration validation
│ └── test_alerts.py # Tests for alert module
│
├── /docs # Documentation files
│ ├── README.md
│ ├── installation.md
│ ├── usage.md
│ ├── architecture.md
│ ├── test_plan.md
│ ├── contribution.md
│ ├── roadmap.md
│ ├── changelog.md
│ ├── code_of_conduct.md
│ ├── license.md
│ └── structure.md


---

## 🔍 Folder/File Descriptions

| Path                   | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `main.py`              | Starts the monitoring process and loads configuration                      |
| `config.yaml`          | User-defined paths, canary files, and alert settings                        |
| `requirements.txt`     | Lists all required Python packages (`watchdog`, `pyyaml`, etc.)             |
| `/src/monitor.py`      | Handles file system monitoring using `watchdog`                             |
| `/src/detector.py`     | Checks for modifications, deletions, and triggers alerts                    |
| `/src/alert.py`        | Executes actions like email alerts or system shutdown                      |
| `/logs/activity.log`   | Auto-generated log file for all detected activity                           |
| `/test/`               | Folder for unit tests that ensure code correctness                         |
| `/docs/`               | Markdown files that document the project’s purpose, usage, and design       |

---

## 📌 Best Practices

- Keep your `config.yaml` backed up for production deployments.
- Always run `pytest` inside the `/test` folder before pushing changes.
- Store additional screenshots and diagrams inside `docs/screenshots/` or `docs/diagrams/`.

---

## 🙌 Maintainer

Developed and maintained by **Ruchir Ganatra**  
🔗 [GitHub](https://github.com/Ranchiro) | [Medium](https://ruchirganatra.medium.com) | [Linktree](https://linktr.ee/ruchir.ganatra)
