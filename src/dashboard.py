"""
dashboard.py – Beispiel für ein einfaches Dashboard mit Streamlit
"""
import streamlit as st
import json

def show_dashboard(results_file="results.json"):
    st.title("Social Media Analyse Dashboard")
    try:
        with open(results_file) as f:
            results = json.load(f)
        st.write("Analyseergebnisse:")
        st.dataframe(results)
        st.bar_chart([r["prediction"] for r in results])
    except Exception as e:
        st.error(f"Fehler beim Laden der Ergebnisse: {e}")

# Beispielaufruf:
# streamlit run src/dashboard.py
