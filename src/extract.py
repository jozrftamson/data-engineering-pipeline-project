"""
extract.py – Extraktion von Social-Media-Beiträgen (z. B. LinkedIn)
"""
import requests

def fetch_posts(api_url, token):
    """Beispiel: Beiträge per API abrufen."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()

# Beispielaufruf (Platzhalter):
# posts = fetch_posts("https://api.linkedin.com/v2/posts", "<TOKEN>")
