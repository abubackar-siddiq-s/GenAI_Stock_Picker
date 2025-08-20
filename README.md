# 📈 GenAI Stock Picker

An AI-powered Streamlit app that helps you discover the **top 5 long-term stocks** from major global stock indexes.  
Simply choose a country → see its popular benchmark index → and get AI-curated stock picks with one-line insights.

---

## 🚀 Features

- 🌍 **Global Coverage**: Supports 30+ countries across **North America, Europe, Asia, Middle East, South America, and Africa**.  
- 📊 **Popular Indexes**: Automatically selects the most recognized index from each country (e.g., **S&P 500** for the US, **BSE Sensex** for India).  
- 🏆 **Top 5 Stocks**: Provides **stock names with one-line long-term investment rationale**.  
- ⚡ **Powered by Google Gemini**: Uses the `gemini-1.5-flash-latest` model for reliable and fast results.  
- 🎯 **Focused on Long-Term**: No trading noise, only long-term fundamentals.  

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Google Generative AI (Gemini API)](https://ai.google.dev/)  

---

## 📂 Project Structure

```
GenAI_Stock_Picker/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── .streamlit/
    └── secrets.toml      # API key (not committed to Git)
```

---

## 🔑 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/GenAI_Stock_Picker.git
cd GenAI_Stock_Picker
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your Gemini API Key

#### Option A: Streamlit Secrets (Recommended)
1. Create a folder named `.streamlit` in your project root.  
2. Inside, create a file named `secrets.toml`.  
3. Add your Gemini API key:
   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```

#### Option B: Environment Variable
```bash
export GEMINI_API_KEY="your_api_key_here"   # Mac/Linux
setx GEMINI_API_KEY "your_api_key_here"     # Windows
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.  

---

## 🌍 Supported Countries & Indexes

- **North America**: US (S&P 500), Canada (S&P/TSX), Mexico (IPC)  
- **Europe**: UK (FTSE 100), Germany (DAX 40), France (CAC 40), Italy (FTSE MIB), Spain (IBEX 35), Switzerland (SMI), Netherlands (AEX), Sweden (OMX 30)  
- **Asia**: India (BSE Sensex), China (SSE Composite), Japan (Nikkei 225), Hong Kong (Hang Seng), South Korea (KOSPI), Singapore (STI), Taiwan (TAIEX), Indonesia (IDX), Malaysia (KLCI), Thailand (SET)  
- **Middle East**: UAE (ADX), Saudi Arabia (TASI), Qatar (QE Index), Kuwait (Premier Market Index)  
- **South America**: Brazil (Bovespa), Argentina (MERVAL), Chile (IPSA)  
- **Africa**: South Africa (JSE ALSI), Egypt (EGX 30), Nigeria (NSE All Share)  

---

## 🧠 Example Usage

1. Select **India**.  
2. App shows **BSE Sensex**.  
3. Click **Get Top 5 Stocks**.  
4. Output:  
   ```
   1. Reliance Industries – Diversified energy & telecom leader with long-term growth.
   2. HDFC Bank – Stable financial institution with consistent earnings.
   3. Infosys – Global IT leader riding digital transformation wave.
   4. TCS – Reliable IT services company with global presence.
   5. Hindustan Unilever – FMCG giant with steady demand across cycles.
   ```

---

## ⚠️ Disclaimer

This app is for **educational and informational purposes only**.  
It should **not** be considered as financial advice. Always do your own research or consult a licensed financial advisor before investing.  

---

## 👨‍💻 Author
**Abubackar Siddiq**  
A passionate developer exploring **GenAI + Finance** 🚀  