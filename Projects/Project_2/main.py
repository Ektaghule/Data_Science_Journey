import io
import os

import PyPDF2
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not found in your .env file.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="AI Resume Roaster",
)

st.title(" AI Resume Roaster")
st.divider()

st.badge("Created by Ekta Ghule")
st.write("Upload your resume and get an AI-powered roast with actionable feedback!")

uploaded_file = st.file_uploader(
    "Upload your Resume (.pdf or .txt)",
    type=["pdf", "txt"],
)

job_role = st.text_input("Target Job Role")

analyze = st.button(" Roast My Resume")


# -----------------------------
# PDF Text Extraction
# -----------------------------
def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(file_bytes)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_text(uploaded_file):
    file_type = uploaded_file.type

    if file_type == "application/pdf":
        file_bytes = io.BytesIO(uploaded_file.read())
        return extract_text_from_pdf(file_bytes)

    elif file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")

    return ""


# -----------------------------
# AI Resume Roast
# -----------------------------
if uploaded_file and analyze:

    if not job_role.strip():
        st.warning("Please enter the target job role.")
        st.stop()

    try:

        file_content = extract_text(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file contains no readable text.")
            st.stop()

        prompt = f"""
You are a brutally honest HR expert with over 20 years of experience.

Roast this resume as if you're performing stand-up comedy.

Rules:
- Be funny.
- Be sarcastic.
- Be brutally honest.
- Don't insult the person personally.
- Point out weaknesses in the resume.
- Mention what recruiters would think.
- Give practical improvements.
- End with a motivational one-liner.

The person is applying for the role:

{job_role}

Resume:

{file_content}

Keep your response under 200 words.
"""

        with st.spinner("Analyzing Resume... "):

            model = genai.GenerativeModel("models/gemini-3.6-flash")

            response = model.generate_content(prompt)

        st.success("Analysis Complete!")

        st.subheader("AI Resume Roast")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"Error: {e}")