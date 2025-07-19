import os
import textract

ALLOWED_EXT = [".pdf", ".docx", ".txt"]

def load_resumes_from_folder(uploaded_files):
    resumes = {}
    for file in uploaded_files:
        ext = os.path.splitext(file.name)[-1].lower()
        if ext in ALLOWED_EXT:
            resumes[file.name] = file.read().decode("utf-8", errors="ignore")
    return resumes

def extract_text_from_jd(jd_input):
    return jd_input.strip()