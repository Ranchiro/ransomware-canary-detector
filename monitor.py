# Watchdog observers
import time
import logging
import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.detector import detect_modifications, load_initial_hashes

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Load configuration
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

class CanaryMonitor(FileSystemEventHandler):
    def on_modified(self, event):
        logger.info("📄 Change detected: %s", event.src_path)
        detect_modifications()

    def on_deleted(self, event):
        logger.info("🗑️ Deletion detected: %s", event.src_path)
        detect_modifications()

def start_monitoring():
    observer = Observer()
    paths = config.get("watch_paths", [])
    
    if not paths:
        logger.error("❌ No watch paths configured.")
        return

    event_handler = CanaryMonitor()

    for path in paths:
        observer.schedule(event_handler, path, recursive=True)
        logger.info("🔍 Monitoring started on: %s", path)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("🛑 Monitoring stopped.")
    observer.join()
