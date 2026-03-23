"""
test_transform.py – Tests für transform.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import pytest
from src.transform import clean_text, extract_features

def test_clean_text_removes_urls():
    text = "Das ist ein Test https://example.com"
    assert "http" not in clean_text(text)

def test_extract_features_counts():
    post = {"text": "#AI ist spannend! #Data"}
    features = extract_features(post)
    assert features["text_length"] == len(post["text"])
    assert features["num_hashtags"] == 2
