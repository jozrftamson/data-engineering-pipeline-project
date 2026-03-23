"""
test_main.py – Integrationstest für die Pipeline
"""
import os
import json
import pytest
import subprocess

def test_pipeline_creates_results_file():
    # Entferne evtl. alte Datei
    if os.path.exists("results.json"):
        os.remove("results.json")
    # Pipeline ausführen
    subprocess.run(["python", "main.py"], check=True)
    # Prüfe, ob Datei erzeugt wurde
    assert os.path.exists("results.json")
    # Prüfe Inhalt
    with open("results.json") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert all("post_id" in r and "prediction" in r for r in data)
