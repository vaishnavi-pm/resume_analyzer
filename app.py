import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")


# Extract text from PDF
def extract_text(pdf_file):
    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text


# Generate Research Gap Analysis
def analyze_research_gap(text):

    prompt = f"""
    You are an expert research analyst.

    Analyze the following research papers and provide:

    1. Main Research Topics
    2. Existing Methodologies
    3. Key Findings
    4. Limitations of Existing Studies
    5. Research Gaps Identified
    6. Future Research Opportunities
    7. Novel Research Ideas

    Research Papers:
    {text[:25000]}
    """

    response = model.generate_content(prompt)

    return response.text


# Streamlit UI
st.set_page_config(page_title="Research Gap Analyzer")

st.title("📚 AI Research Gap Analyzer")

uploaded_files = st.file_uploader(
    "Upload Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    combined_text = ""

    with st.spinner("Extracting papers..."):
        for file in uploaded_files:
            combined_text += extract_text(file)
            combined_text += "\n\n"

    st.success("PDFs Processed Successfully")

    if st.button("Analyze Research Gap"):

        with st.spinner("Analyzing Research Papers..."):
            result = analyze_research_gap(combined_text)

        st.subheader("Research Gap Analysis")
        st.write(result)

        st.download_button(
            "Download Report",
            result,
            file_name="research_gap_report.txt"
        )