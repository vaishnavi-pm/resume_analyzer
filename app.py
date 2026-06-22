import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#111827,
#1e293b
);
color:white;
}

h1,h2,h3{
color:white;
}

.block-container{
padding-top:2rem;
}

.card{
background: rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
backdrop-filter: blur(15px);
box-shadow:0 8px 32px rgba(0,0,0,0.3);
margin-bottom:20px;
}

.score{
font-size:60px;
font-weight:bold;
text-align:center;
color:#00FFB2;
}

.preview{
background:#111827;
padding:20px;
border-radius:15px;
height:350px;
overflow-y:auto;
border:1px solid #334155;
}

.badge{

display:inline-block;

padding:8px 15px;

margin:5px;

background:#2563EB;

border-radius:20px;

color:white;

font-weight:500;

}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------

st.markdown("""
<h1 style='text-align:center;font-size:55px;'>
🤖 AI Resume Analyzer
</h1>

<p style='text-align:center;
font-size:22px;
color:#B0B0B0;'>

Get ATS Score, Skills Analysis and Career Suggestions Instantly

</p>

""", unsafe_allow_html=True)

st.write("")

# ---------- INPUT ----------

col1, col2 = st.columns(2)

with col1:

    resume_file = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:

    job_description = st.text_area(
        "📝 Enter Job Description",
        height=200,
        placeholder="""
Python Developer

Skills Required:

- Python
- SQL
- Machine Learning
- Data Analysis
- Git
        """
    )

# ---------- PDF TEXT ----------

def extract_text(pdf_file):

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text

    return text

# ---------- ANALYSIS ----------

if resume_file and job_description:

    resume_text = extract_text(resume_file)

    documents = [resume_text, job_description]

    cv = CountVectorizer()

    matrix = cv.fit_transform(documents)

    similarity = cosine_similarity(matrix)[0][1] * 100

    st.write("")

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📊 Analysis Result")

    st.markdown(

        f"""

        <div class='score'>

        {similarity:.2f}%

        </div>

        """,

        unsafe_allow_html=True

    )

    st.progress(similarity/100)

    st.write("")

    if similarity > 80:

        st.success("🔥 Excellent Match")

    elif similarity > 60:

        st.info("👍 Good Match")

    else:

        st.error("⚠ Needs Improvement")

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- SKILLS ----------

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🛠 Skills")

    skills = [

        "Python",

        "SQL",

        "Machine Learning",

        "React",

        "Laravel",

        "MySQL",

        "Git"

    ]

    badges = ""

    for skill in skills:

        badges += f"<span class='badge'>{skill}</span>"

    st.markdown(badges, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- RESUME PREVIEW ----------

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📄 Resume Preview")

    st.markdown(

        f"""

        <div class='preview'>

        <pre style='

        white-space:pre-wrap;

        color:white;

        font-size:15px;

        font-family:Poppins;

        '>

        {resume_text[:3000]}

        </pre>

        </div>

        """,

        unsafe_allow_html=True

    )

    st.markdown("</div>", unsafe_allow_html=True)