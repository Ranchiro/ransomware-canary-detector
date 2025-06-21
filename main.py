# Entry point for Ransomware Canary Detector
from src.monitor import start_monitoring
from src.detector import load_initial_hashes

if __name__ == "__main__":
    print("🚨 Ransomware Canary Detector started.")
    load_initial_hashes()
    start_monitoring()
