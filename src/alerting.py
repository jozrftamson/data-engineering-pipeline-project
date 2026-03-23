"""
alerting.py – Beispiel für einfaches Alerting per E-Mail (Platzhalter)
"""
import smtplib
from email.message import EmailMessage
import os

def send_alert(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = os.environ.get("ALERT_EMAIL_FROM", "alert@example.com")
    msg["To"] = to_email
    # Platzhalter: SMTP-Server und Authentifizierung anpassen
    # with smtplib.SMTP("smtp.example.com", 587) as server:
    #     server.starttls()
    #     server.login("user", "password")
    #     server.send_message(msg)
    print(f"ALERT: {subject} -> {to_email}")

# Beispielaufruf:
# send_alert("Pipeline-Fehler", "Fehlerdetails...", "admin@example.com")
