# app.py

import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# Get API key
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found. Please set it in Streamlit secrets or as an environment variable.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel('gemini-2.5-flash')

# --- Streamlit UI ---
st.set_page_config(page_title="AI Stock Picker", page_icon="🌍", layout="centered")

st.title("📈 AI Stock Picker")
st.caption("Top 5 long-term stock ideas from major world markets")

# --- Country Selection ---
countries = {
    # 🌎 North America
    "United States": "S&P 500",
    "Canada": "S&P/TSX Composite Index",
    "Mexico": "IPC (Índice de Precios y Cotizaciones)",

    # 🌍 Europe
    "United Kingdom": "FTSE 100",
    "Germany": "DAX 40",
    "France": "CAC 40",
    "Italy": "FTSE MIB",
    "Spain": "IBEX 35",
    "Switzerland": "SMI (Swiss Market Index)",
    "Netherlands": "AEX",
    "Sweden": "OMX Stockholm 30",

    # 🌏 Asia
    "India": "BSE Sensex",
    "China": "SSE Composite",
    "Japan": "Nikkei 225",
    "Hong Kong": "Hang Seng Index",
    "South Korea": "KOSPI",
    "Singapore": "Straits Times Index (STI)",
    "Taiwan": "TAIEX",
    "Indonesia": "IDX Composite (IHSG)",
    "Malaysia": "FTSE Bursa Malaysia KLCI",
    "Thailand": "SET Index",

    # 🌐 Middle East
    "United Arab Emirates": "ADX General",
    "Saudi Arabia": "Tadawul All Share Index (TASI)",
    "Qatar": "QE Index",
    "Kuwait": "Premier Market Index",

    # 🌎 South America
    "Brazil": "Bovespa (Ibovespa)",
    "Argentina": "MERVAL",
    "Chile": "IPSA",

    # 🌍 Africa
    "South Africa": "FTSE/JSE All Share Index (JSE ALSI)",
    "Egypt": "EGX 30",
    "Nigeria": "NSE All Share Index"
}

selected_country = st.selectbox("🌍 Select a country", list(countries.keys()))

if selected_country:
    selected_index = countries[selected_country]
    st.subheader(f"📊 Popular Index: {selected_index}")

    if st.button("🔎 Get Top 5 Stocks"):
        with st.spinner("Fetching stock picks..."):
            try:
                prompt = f"""
                You are a confident financial assistant.
                List exactly **5 top long-term stocks** from the {selected_index} index in {selected_country}.
                
                Rules:
                - Only show stock name + one short line why it’s good for long-term investing.
                - Do NOT include ticker symbols, disclaimers, or "I cannot actually tell" type answers.
                - Keep the format clean as a numbered list (1–5).
                """

                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
# --- End of Streamlit UI ---
