import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Set Streamlit app title
st.title("📈 Global Stock Picker")

# Sidebar: Select a country
country = st.sidebar.selectbox(
    "Pick a Country",
    ("India", "United States", "United Kingdom", "Japan", "Germany", "China", "France", "Australia", "Canada", "Singapore")
)

# Set your Gemini API key
api_key = "AIzaSyAJzNRZGPKS8kxEIOxPtXtSbOmFrWoGTKo"

# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key,
    temperature=0.7
)

# Define function to generate index and stocks
def generate_index_and_stocks(country):
    # Prompt for index name
    prompt_template_index = PromptTemplate(
        input_variables=['country'],
        template="I want to invest in stocks from {country}. Suggest one major stock market index for that country. Only one index name, no explanations."
    )

    index_chain = LLMChain(llm=llm, prompt=prompt_template_index, output_key="index_name")

    # Prompt for stock suggestions
    prompt_template_stocks = PromptTemplate(
        input_variables=['index_name'],
        template="List 10 large, financially stable companies from the {index_name} index that are commonly regarded as strong long-term performers based on publicly available financial metrics and historical stability. Return only the company names, one per line."
    )

    stocks_chain = LLMChain(llm=llm, prompt=prompt_template_stocks, output_key="stock_items")

    # Sequential chain
    chain = SequentialChain(
        chains=[index_chain, stocks_chain],
        input_variables=['country'],
        output_variables=['index_name', 'stock_items'],
        verbose=False
    )

    response = chain({'country': country})
    return response

# Main app logic
if country:
    with st.spinner("Generating stock market suggestions..."):
        response = generate_index_and_stocks(country)

    st.header(f"📊 Index: {response['index_name'].strip()}")
    st.subheader("Top 10 Companies:")
    stock_list = response['stock_items'].strip().split("\n")
    for stock in stock_list:
        st.write("-", stock)