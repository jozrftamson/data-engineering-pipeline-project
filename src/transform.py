"""
transform.py – Transformation & KI-Anreicherung von Social-Media-Beiträgen
"""
import re

def clean_text(text):
    """Einfache Textbereinigung (z. B. Entfernen von URLs)."""
    return re.sub(r"https?://\S+", "", text)

def extract_features(post):
    """Feature Engineering: Beispiel für Textlänge und Hashtag-Zahl."""
    text = post.get("text", "")
    features = {
        "text_length": len(text),
        "num_hashtags": text.count("#"),
    }
    return features

# Beispielaufruf:
# features = extract_features({"text": "#AI ist spannend! #Data"})
