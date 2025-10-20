import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import google.generativeai as genai
import os

# --- CONFIG ---
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("Gemini API key missing.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# --- PAGE SETUP ---
st.set_page_config(page_title="Global Market Insights", layout="wide")
st.title("🌎 AI Global Market Insights Dashboard")
st.caption("Interactive multi-market analysis with AI insights & news")

# --- MARKET OPTIONS ---
indices = {
    "India (NIFTY 50)": "^NSEI",
    "USA (S&P 500)": "^GSPC",
    "Japan (Nikkei 225)": "^N225",
    "UK (FTSE 100)": "^FTSE",
    "Germany (DAX)": "^GDAXI",
    "China (SSE Composite)": "000001.SS"
}

selected_markets = st.multiselect(
    "📊 Select Markets to Compare (up to 3)", list(indices.keys()), default=["India (NIFTY 50)"]
)

# --- EXPANDED TIMEFRAMES ---
timeframes = {
    "1 Week": 7,
    "2 Weeks": 14,
    "1 Month": 30,
    "3 Months": 90,
    "6 Months": 180,
    "1 Year": 365,
    "2 Years": 730,
    "3 Years": 1095,
    "5 Years": 1825,
    "10 Years": 3650,
    "Max (All Available)": None
}
selected_timeframe = st.selectbox("⏳ Select Timeframe", list(timeframes.keys()))
days = timeframes[selected_timeframe]

# --- FETCH DATA ---
market_data = {}
for market in selected_markets:
    ticker = indices[market]
    try:
        df = yf.download(ticker, period="max")  # Always fetch max
        if not df.empty and 'Close' in df.columns:
            series = df['Close']
            series.name = market
            market_data[market] = series
        else:
            st.warning(f"No data found for {market}. Skipping.")
    except Exception as e:
        st.warning(f"Error fetching {market}: {e}")

if not market_data:
    st.error("No valid market data available for the selected markets.")
    st.stop()

# --- ALIGN DATA ---
combined_df = pd.concat(market_data.values(), axis=1)
combined_df.columns = list(market_data.keys())

# Handle timeframe selection
if days is not None:
    combined_df = combined_df.tail(days)  # Keep only selected timeframe

combined_df = combined_df.ffill()  # Forward-fill missing values

# --- NORMALIZE DATA FOR FAIR COMPARISON ---
normalized_df = combined_df.copy()
for market in normalized_df.columns:
    normalized_df[market] = (normalized_df[market] / normalized_df[market].iloc[0]) * 100

# --- PLOT NORMALIZED MULTI-MARKET CHART ---
fig = go.Figure()
for market in normalized_df.columns:
    fig.add_trace(go.Scatter(
        x=normalized_df.index,
        y=normalized_df[market],
        mode='lines',
        name=market
    ))

fig.update_layout(
    title=f"Market Trend Comparison ({selected_timeframe}) — Normalized",
    xaxis_title="Date",
    yaxis_title="Index Value (Normalized to 100)",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# --- AI Summary & News ---
for market, series in market_data.items():
    with st.spinner(f"Generating AI insights for {market}..."):
        # Fetch latest 3 headlines via yfinance
        try:
            ticker_obj = yf.Ticker(indices[market])
            news_items = ticker_obj.news[:3]
            news_text = "\n".join([f"- {n['title']}" for n in news_items])
        except:
            news_text = "No news available."

        prompt = f"""
        You are a professional market analyst.
        Analyze the last {days if days else 'all available'} days of {market} index (closing prices):
        {series.tail(10).to_string()}

        Summarize:
        1. Trend (bullish/bearish/sideways)
        2. Key sectors driving trend (general knowledge)
        3. Market sentiment (Fear / Neutral / Greed)
        4. Short motivational investing insight
        5. Summarize latest 3 news headlines:
        {news_text}

        Format:
        📈 Market Summary:
        🧠 Reason:
        🔥 Sentiment:
        💡 Insight:
        📰 News:
        """

        try:
            response = model.generate_content(prompt)
            st.markdown(f"### {market}")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"AI summary error for {market}: {e}")
