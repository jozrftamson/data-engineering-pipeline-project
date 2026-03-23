"""
alerting_pagerduty.py – Beispiel für PagerDuty-Integration
"""
import os
import requests

def send_pagerduty_alert(summary, severity="error"):
    api_key = os.environ.get("PAGERDUTY_API_KEY")
    service_id = os.environ.get("PAGERDUTY_SERVICE_ID")
    if not api_key or not service_id:
        print("PagerDuty-Konfiguration fehlt.")
        return
    url = "https://events.pagerduty.com/v2/enqueue"
    payload = {
        "routing_key": service_id,
        "event_action": "trigger",
        "payload": {
            "summary": summary,
            "severity": severity,
            "source": "data-pipeline"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print(f"PagerDuty-Alert gesendet: {response.status_code}")

# Beispielaufruf:
# send_pagerduty_alert("Pipeline-Fehler: Modelltraining fehlgeschlagen")
