# Detection logic for canary triggers
import os
import time
import hashlib
import logging
import yaml
from src.alert import trigger_alert

# Load config
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Cache initial canary file hashes
file_hashes = {}

def hash_file(path):
    """Returns SHA-256 hash of a file."""
    try:
        with open(path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        return None

def load_initial_hashes():
    for path in config.get("canary_files", []):
        file_hashes[path] = hash_file(path)

def detect_modifications():
    for path in config.get("canary_files", []):
        if not os.path.exists(path):
            trigger_alert(f"❌ Canary file deleted: {path}")
            continue

        new_hash = hash_file(path)
        if file_hashes.get(path) and file_hashes[path] != new_hash:
            trigger_alert(f"⚠️ Canary file modified: {path}")
