import re

def highlight_keywords(jd_text, resume_text, color="#ffd54f"):
    jd_keywords = set(jd_text.lower().split())
    highlighted = []
    for word in resume_text.split():
        if word.lower() in jd_keywords:
            highlighted.append(f"<mark style='background-color:{color}'>{word}</mark>")
        else:
            highlighted.append(word)
    return " ".join(highlighted)