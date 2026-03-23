"""
main.py – Orchestrierung der Pipeline für Social-Media-Analyse
"""
from src.extract import fetch_posts # pyright: ignore[reportUnusedImport]
from src.monitoring import log_event
from src.transform import clean_text, extract_features
from src.model import train_model, predict
from src.load import save_results
import numpy as np

# Schritt 1: Beiträge extrahieren (Platzhalter)
log_event("Pipeline gestartet")
posts = [
    {"id": 1, "text": "#AI ist spannend! #Data https://example.com"},
    {"id": 2, "text": "Neue Features für #LinkedIn Nutzer."},
]

# Schritt 2: Transformation & Feature Engineering
log_event("Transformation & Feature Engineering", details=f"{len(posts)} Beiträge")
features = [extract_features({"text": clean_text(p["text"])}) for p in posts]
X = np.array([[f["text_length"], f["num_hashtags"]] for f in features])

y = np.array([1, 0])  # Beispiel-Labels: 1 = hohe Reichweite, 0 = gering

# Schritt 3: Modell trainieren
log_event("Modelltraining", details=f"{X.shape[0]} Samples")
model = train_model(X, y)

# Schritt 4: Vorhersagen für neue Beiträge
log_event("Vorhersage", details=f"{len(predictions)} Beiträge")
predictions = predict(model, X)

# Schritt 5: Ergebnisse speichern
log_event("Ergebnisse gespeichert", details="results.json")
results = [{"post_id": p["id"], "prediction": int(pred)} for p, pred in zip(posts, predictions)]
save_results(results)

print("Analyse abgeschlossen. Ergebnisse gespeichert.")
