import os
import streamlit as st
from langchain.llms import OpenAI

# Set your OpenAI API key (best to use a Streamlit secret or environment variable in production)
os.environ['OPENAI_API_KEY'] = "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"  # <-- Replace with your real API key

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
                # Initialize LangChain LLM
                llm = OpenAI(temperature=0.6)
                response = llm(user_prompt)
                st.success("Here are your stock suggestions:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
