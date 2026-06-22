import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Resume Analyzer")

st.title("📄 AI Resume Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area(
    "Enter Job Description",
    height=200
)

def extract_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

if resume_file and job_description:
    resume_text = extract_text(resume_file)

    documents = [resume_text, job_description]

    cv = CountVectorizer()
    matrix = cv.fit_transform(documents)

    similarity = cosine_similarity(matrix)[0][1] * 100

    st.subheader("Analysis Result")

    st.write(f"Resume Match Score: **{similarity:.2f}%**")

    if similarity > 70:
        st.success("Excellent Match")
    elif similarity > 50:
        st.warning("Good Match")
    else:
        st.error("Needs Improvement")

    st.subheader("Resume Preview")
    st.write(resume_text[:3000])
