import streamlit as st
import time
from file_processor import process_file
from rag_pipeline import chunk_text, generate_answer # <--- Must match rag_pipeline.py
from embeddings import get_embeddings
from vector_store import VectorStore



st.title(" AI RAG Assistant")

# Sidebar for Provider Selection
provider = st.sidebar.radio("Select Roast (LLM):", ["Gemini", "OpenAI"])
model_choice = "gemini/gemini-2.0-flash" if provider == "Gemini" else "openai/gpt-4o"

uploaded_files = st.file_uploader("Drop your files here", accept_multiple_files=True)

if uploaded_files and st.button("Brew Context"):
    progress_bar = st.progress(0, text="Starting the brew...")
    
    # 1. Reading Files (25%)
    full_text = ""
    for file in uploaded_files:
        full_text += process_file(file) + "\n"
    progress_bar.progress(25, text="Reading files... 25%")
    
    # 2. Chunking (50%)
    chunks = chunk_text(full_text)
    progress_bar.progress(50, text="Grinding text into chunks... 50%")
    
    # 3. Embedding (75%)
    embeddings = get_embeddings(chunks)
    progress_bar.progress(75, text="Extracting flavor (Embeddings)... 75%")
    
    # 4. Storing (100%)
    dimension = len(embeddings[0])
    st.session_state.vector_store = VectorStore(dimension)
    st.session_state.vector_store.add_vectors(embeddings, chunks)
    progress_bar.progress(100, text="✅ Brew Ready!")
    time.sleep(1)
    progress_bar.empty()

question = st.text_input("Ask a question:")
if question and st.session_state.get("vector_store"):
    with st.spinner(f"Generating {provider} response..."):
        answer = generate_answer(question, st.session_state.vector_store, model_choice)
    st.markdown(f"### ☕ {provider} Says:")
    st.write(answer)