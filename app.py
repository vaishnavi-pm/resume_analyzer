import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")


# Extract text from PDF
def extract_text(pdf_file):

    text = ""

    pdf = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text


# Analyze Resume
def analyze_resume(text):

    prompt = f"""
You are an expert ATS Resume Reviewer and Career Advisor.

Analyze the following resume and provide:

1. Candidate Summary

2. Technical Skills Identified

3. Strengths of the Resume

4. Weaknesses / Missing Information

5. ATS Score (out of 100)

6. Suggestions to Improve ATS Score

7. Recommended Projects

8. Recommended Certifications

9. Suitable Job Roles

10. Overall Feedback

Resume:

{text[:25000]}
"""

    response = model.generate_content(prompt)

    return response.text


# Streamlit Page Settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)


# Title
st.title("📄 AI Resume Analyzer")
st.write("Upload your Resume PDF and get ATS analysis using Gemini AI.")


# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


# If file uploaded
if uploaded_file:

    with st.spinner("Extracting Resume..."):

        resume_text = extract_text(uploaded_file)

    st.success("Resume Processed Successfully ✅")


    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(resume_text)

        st.subheader("Resume Analysis Report")

        st.write(result)

        st.download_button(
            label="Download Report",
            data=result,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )
