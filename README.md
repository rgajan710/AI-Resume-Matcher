# 🚀 AI-Powered Resume Matcher

An intelligent resume ranking tool that matches multiple resumes to a job description using state-of-the-art NLP embeddings and semantic search.

---

## 🔍 What It Does

- Upload multiple resumes (PDF/DOCX/TXT)
- Paste or upload a Job Description
- Uses Sentence-BERT (all-MiniLM-L6-v2) to encode text
- Stores resume embeddings in a FAISS vector index
- Ranks resumes using cosine similarity
- Highlights keyword overlap between JD and resumes
- Displays top matches with scores and download options

---

## 📁 Folder Structure

```bash
resume-matcher-streamlit/
├── app.py                       # Main Streamlit app
├── requirements.txt            # Python dependencies
├── config.yaml                 # Model and UI configuration
├── data/                       # Sample resumes and JDs
│   ├── resumes/
│   ├── job_descriptions/
│   └── processed/
├── src/                        # Core logic modules
│   ├── preprocessing.py
│   ├── embedding.py
│   ├── similarity.py
│   ├── keyword_highlighter.py
│   └── utils.py
├── .streamlit/
│   └── config.toml             # Streamlit UI settings
└── README.md
```

---

## 💡 How It Works

1. Resumes and JD are cleaned, lowercased, stopwords removed, and lemmatized
2. Sentence-BERT model creates dense vector embeddings
3. Resumes are stored in FAISS index
4. JD is embedded and compared to stored vectors via cosine similarity
5. Top N matching resumes are ranked and displayed with highlights

---

## 🧪 Example Usage

```bash
streamlit run app.py
```

Go to `http://localhost:8501` and upload resumes and a job description.

---

## ⚙️ Configuration (config.yaml)

```yaml
model:
  name: all-MiniLM-L6-v2
similarity:
  threshold: 0.6
  top_k: 5
ui:
  title: "AI Resume Matcher"
  description: "Match resumes against your job descriptions with AI."
```

---

## 🚀 Deployment

To deploy on **Streamlit Cloud**:

1. Push to a GitHub repo
2. Connect the repo to Streamlit Cloud
3. Set Python version and dependencies

---

## 📦 Requirements

```txt
streamlit
sentence-transformers
faiss-cpu
nltk
python-docx
pdfplumber
PyYAML
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📄 License

[MIT License](LICENSE)

---

## 👨‍💻 Author

**Rohan G** 

---


