from src.alert import trigger_alert

def test_email():
    try:
        trigger_alert("This is a test alert.")
        print("✅ Email alert test passed.")
    except Exception as e:
        print(f"❌ Email alert test failed: {e}")
