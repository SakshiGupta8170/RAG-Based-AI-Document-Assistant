from sentence_transformers import SentenceTransformer

# Load model once globally to avoid re-loading on every call
# This uses a small, fast model ideal for local RAG
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text_chunks):
    """
    Create embeddings using SentenceTransformers.
    Returns a list of vectors.
    """
    if isinstance(text_chunks, str):
        text_chunks = [text_chunks]
        
    embeddings = model.encode(text_chunks)
    return embeddings