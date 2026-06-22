# 📄 AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange?style=for-the-badge\&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An AI-powered Resume Analyzer that evaluates resumes, calculates an ATS score, identifies strengths and weaknesses, and provides personalized career recommendations using Google's Gemini AI.

---

## ✨ Features

* 📂 Upload Resume in PDF format
* 🤖 AI-powered Resume Analysis using Gemini
* 📊 ATS Score Evaluation
* 🛠️ Technical Skills Extraction
* ✅ Resume Strengths & Weaknesses
* 💡 Resume Improvement Suggestions
* 🚀 Recommended Projects
* 🎓 Recommended Certifications
* 💼 Suitable Job Roles
* 📥 Download Analysis Report

---

## 🛠️ Tech Stack

| Technology    | Usage                 |
| ------------- | --------------------- |
| Python        | Programming Language  |
| Streamlit     | Web Framework         |
| Gemini AI     | Resume Analysis       |
| PyMuPDF       | PDF Text Extraction   |
| Generative AI | AI Content Generation |

---

## 📂 Project Structure

```bash
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API Key

Open `app.py`

Replace:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

with

```python
genai.configure(api_key="YOUR_API_KEY")
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 📊 Output

The application generates:

* Candidate Summary
* Technical Skills
* Resume Strengths
* Resume Weaknesses
* ATS Score
* Improvement Suggestions
* Recommended Projects
* Recommended Certifications
* Suitable Job Roles
* Overall Feedback

---

## 🎯 Future Enhancements

* Resume vs Job Description Matching
* LinkedIn Profile Analyzer
* Resume Keyword Optimization
* Export Report as PDF
* Resume Builder
* Multiple Resume Comparison

---

## ⭐ Show Your Support

If you like this project:

⭐ Star this repository
🍴 Fork this repository
📢 Share it with others

---

## 👩‍💻 Author

**Vaishnavi PM**

B.Tech Information Technology

Passionate about AI • MLOps • Web Development • Generative AI 🚀
