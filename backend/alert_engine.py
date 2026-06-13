# backend/alert_engine.py

THRESHOLD = 2000

def check_alert(power):

    if power > THRESHOLD:

        return "HIGH POWER ALERT"

    return "NORMAL"