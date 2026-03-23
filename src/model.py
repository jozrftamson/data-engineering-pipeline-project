"""
model.py – Beispiel für ein einfaches ML-Modell (Klassifikation)
"""
from sklearn.linear_model import LogisticRegression
import numpy as np

def train_model(X, y):
    """Trainiert ein einfaches Klassifikationsmodell."""
    model = LogisticRegression()
    model.fit(X, y)
    return model

def predict(model, X):
    """Gibt Vorhersagen für neue Daten zurück."""
    return model.predict(X)

# Beispiel-Daten (Platzhalter):
# X = np.array([[100, 2], [50, 0]])  # z. B. [Textlänge, Hashtags]
# y = np.array([1, 0])  # 1 = hohe Reichweite, 0 = geringe Reichweite
# model = train_model(X, y)
# prediction = predict(model, np.array([[80, 1]]))
