import streamlit as st
from groq import Groq
import PyPDF2
import io
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Analyser", page_icon="📄", layout="centered")

st.title("AI Resume Analyser")
st.markdown("""
Upload your resume in PDF format, and let our AI analyze it for key skills, experience, and areas of improvement.
""")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TEXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are targeting(optional):")   

analyse = st.button("Analyse Resume")


def extract_text_from_pdf(file_stream):
    pdf_reader = PyPDF2.PdfReader(file_stream)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")


if analyse and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read.")
            st.stop()

        prompt = f"""Analyze the following resume for key skills, experience, and areas of improvement. 
        Focus on the following areas:
        1. Content clarity and impact.
        2. Skills presentation.
        3. Specific improvements for: {job_role if job_role else'general applications'}

        Resume Content: 
        {file_content}

        Please provide your analysis in a clear, structured format with specific suggestions for improvement."""

        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content" : "You are an expert resume reviewer with years of experience in HR and recruitement" },
                {
                    "role": "user", "content" : prompt
                }
            ], temperature=0.7,
            max_tokens=1500   
        )
        st.markdown("### Resume Analysis:")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred during analysis: {str(e)}")
