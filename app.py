import streamlit as st
import os
from src.utils import load_resumes_from_folder, extract_text_from_jd
from src.preprocessing import preprocess_text
from src.embedding import Embedder
from src.similarity import SimilarityEngine
from src.keyword_highlighter import highlight_keywords

st.set_page_config(page_title="AI Resume Matcher")

# Load config
import yaml
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Initialize Embedder and Similarity Engine
embedder = Embedder(config['model']['name'], config['model']['device'])
sim_engine = SimilarityEngine(embedder)

# UI
st.title(config['ui']['title'])

uploaded_resumes = st.file_uploader("Upload resumes (PDF, DOCX, TXT)", accept_multiple_files=True)
jd_input = st.text_area("Paste the job description")

if st.button("Match Resumes") and uploaded_resumes and jd_input:
    jd_text = preprocess_text(jd_input)
    jd_vector = embedder.encode([jd_text])[0]

    resumes = load_resumes_from_folder(uploaded_resumes)
    processed_resumes = [(f, preprocess_text(t)) for f, t in resumes.items()]

    resume_vectors = [embedder.encode([txt])[0] for _, txt in processed_resumes]
    top_matches = sim_engine.get_top_k(jd_vector, resume_vectors, processed_resumes, config['similarity']['top_k'])

    for score, filename, raw_text in top_matches:
        st.markdown(f"### {filename}")
        if config['ui']['show_scores']:
            st.markdown(f"**Match Score**: {score:.2f}")
        if config['highlight']['enable']:
            highlighted = highlight_keywords(jd_text, raw_text, config['highlight']['color'])
            st.markdown(highlighted, unsafe_allow_html=True)
        if config['ui']['show_download_buttons']:
            st.download_button("Download Resume", raw_text, file_name=filename)