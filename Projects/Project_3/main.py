import io
import os
from sys import exception
import pandas as pd
from google import genai
import streamlit as st
from dotenv import load_dotenv


load_dotenv()
st.title("AI Financial Analyzer")
st.divider()
st.badge("Ekta Ghule")
st.markdown("Make better decisions with AI in finance")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not found in your .env file.")
    st.stop()

client = genai.Client(api_key=GEMINI_API_KEY)


uploaded_file = st.file_uploader("Upload your financial data as csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
            
    tab1, tab2, tab3 = st.tabs(["Raw Data", "Cleaned Data", "AI Insights"])

    with tab1:
        st.subheader("Raw Data")
        st.dataframe(df)
            
    with tab2:
        st.subheader("Cleaned Data")
        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
        df.dropna(subset=["Amount"], inplace=True)
        st.dataframe(df)
            
    with tab3:
        st.subheader("Gemini AI Analysis")
        
        prompt = f"""Analyze the following financial data provided in CSV format. The data includes columns for 'Date', 'Category', 'Description', 'Amount', and 'Payment Method'.

    Provide insights based on this data, including:
    1.  A summary of total income and total expenses.
    2.  A breakdown of expenses by category.
    3.  Identification of the most frequently used payment methods.
    4.  Any other interesting observations or patterns you can find in the data.

    Here is the data : {df.to_csv(index=False)}
    """
        
        try:
            with st.spinner("Analyzing Data... "):
                response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)
                st.markdown("## AI Suggestions")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error from Gemini: {str(e)}")
        
            
            