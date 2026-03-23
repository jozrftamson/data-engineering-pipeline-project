"""
alerting_slack.py – Beispiel für Slack-Integration
"""
import os
import requests

def send_slack_alert(message):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("Slack Webhook URL fehlt.")
        return
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    print(f"Slack-Alert gesendet: {response.status_code}")

# Beispielaufruf:
# send_slack_alert("Pipeline erfolgreich abgeschlossen.")
