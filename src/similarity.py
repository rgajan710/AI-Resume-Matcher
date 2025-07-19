import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityEngine:
    def __init__(self, embedder):
        self.embedder = embedder

    def get_top_k(self, jd_vec, resume_vecs, processed_resumes, k):
        scores = cosine_similarity([jd_vec], resume_vecs)[0]
        results = sorted(zip(scores, [r[0] for r in processed_resumes], [r[1] for r in processed_resumes]), reverse=True)
        return results[:k]