"""
monitoring.py – Beispiel für einfaches Logging und Monitoring
"""
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def log_event(event, details=None):
    msg = f"EVENT: {event}"
    if details:
        msg += f" | Details: {details}"
    logging.info(msg)

# Beispielaufruf:
# log_event("Pipeline gestartet")
