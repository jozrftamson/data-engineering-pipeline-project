"""
load.py – Laden der Analyseergebnisse in ein Zielsystem (z. B. Datenbank)
"""
import json

def save_results(results, filename="results.json"):
    """Speichert Analyseergebnisse als JSON-Datei."""
    with open(filename, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

# Beispielaufruf:
# save_results([{"post_id": 1, "prediction": 1}])
