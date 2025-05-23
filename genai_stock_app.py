import streamlit as st
from langchain_openai import OpenAI
import os

# Use Streamlit secrets (defined in .streamlit/secrets.toml)
os.environ["OPENAI_API_KEY"] = "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"

# Streamlit UI
st.set_page_config(page_title="GenAI Stock Advisor", page_icon="📈")
st.title("📊 GenAI Stock Advisor")
st.write("Get smart stock suggestions powered by OpenAI and LangChain.")

# User input
user_prompt = st.text_area("Enter your investment interest or ask for stock suggestions:")

if st.button("Suggest Stocks"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating suggestions..."):
            try:
                llm = OpenAI(temperature=0.6)
                response = llm.invoke(user_prompt)
                st.success("Here are your stock suggestions:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
