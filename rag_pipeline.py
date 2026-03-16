import os
import litellm
from dotenv import load_dotenv

load_dotenv()


def chunk_text(text, chunk_size=500):
    """Splits text into chunks of a specified word count."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


def generate_answer(question, vector_store, model_choice):
    """
    Generates an answer using LiteLLM to support both Gemini and OpenAI.
    """
    from embeddings import get_embeddings
    
    # 1. Context Retrieval
    query_embedding = get_embeddings([question])[0]
    context_chunks = vector_store.search(query_embedding)
    context = "\n\n".join(context_chunks)

    prompt = f"Answer ONLY using the context below.\n\nContext:\n{context}\n\nQuestion:\n{question}"

    try:
        # LiteLLM handles the API differences automatically
        response = litellm.completion(
            model=model_choice,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"


