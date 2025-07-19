from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name, device='cpu'):
        self.model = SentenceTransformer(model_name, device=device)

    def encode(self, texts):
        return self.model.encode(texts, convert_to_tensor=False, show_progress_bar=False)
