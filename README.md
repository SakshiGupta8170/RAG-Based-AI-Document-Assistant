# 🤖 DocMind AI — RAG Document Assistant

### Created by **Sakshi Gupta**

DocMind AI is an AI-powered document assistant that allows users to upload files and ask questions about them. The system processes documents such as **PDF, CSV, Excel, and Text files**, converts them into embeddings, and retrieves relevant information using **Retrieval-Augmented Generation (RAG)**.

The application then uses **Google Gemini AI** to generate intelligent answers based on the uploaded documents.

---

# 🚀 Features

* 📂 Upload multiple document types
* 📄 Supports **PDF, CSV, Excel, TXT**
* 🧠 AI-powered **context-based question answering**
* ⚡ Fast semantic search using **FAISS vector database**
* 🔎 Retrieval-Augmented Generation (RAG) pipeline
* 💬 Interactive **Streamlit UI interface**
* 📊 Embeddings created using **SentenceTransformers**

---

# 🧠 How It Works

The system follows a **RAG (Retrieval-Augmented Generation) architecture**:

```
User Uploads Files
        ↓
Text Extraction from Documents
        ↓
Text Chunking
        ↓
SentenceTransformer Embeddings
        ↓
Stored in FAISS Vector Database
        ↓
User Asks Question
        ↓
Relevant Chunks Retrieved
        ↓
Gemini AI Generates Context-Based Answer
```

---

# 🛠️ Tech Stack

| Component       | Technology           |
| --------------- | -------------------- |
| Frontend        | Streamlit            |
| Language        | Python               |
| Embeddings      | SentenceTransformers |
| Vector Database | FAISS                |
| AI Model        | Google Gemini        |
| Data Processing | Pandas, PDFPlumber   |

---

# 📂 Project Structure

```
DocMind-AI-RAG-Assistant
│
├── app.py              # Main Streamlit Application
├── rag_pipeline.py     # RAG logic and Gemini integration
├── embeddings.py       # Text embedding generation
├── vector_store.py     # FAISS vector database handling
├── file_processor.py   # File reading and text extraction
├── requirements.txt    # Project dependencies
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/DocMind-AI-RAG-Assistant.git
```

Navigate into the project folder:

```
cd DocMind-AI-RAG-Assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create a `.env` file in the root directory and add your **Gemini API key**:

```
GEMINI_API_KEY=your_api_key_here
```

⚠️ Do not upload the `.env` file to GitHub.

---

# ▶️ Running the Application

Start the Streamlit application:

```
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# 📸 Example Workflow

1. Upload a document (PDF / CSV / Excel / TXT)
2. The system processes and stores document embeddings
3. Ask a question about the uploaded data
4. AI retrieves relevant information and generates an answer

---

# 🎯 Use Cases

* Document analysis
* Knowledge base assistants
* Research document Q&A
* Business report analysis
* AI-powered file search

---

# 📈 Future Improvements

* Chat history memory
* Multi-user authentication
* Cloud deployment
* OCR support for scanned documents
* Source citation for answers

---

# 👨‍💻 Author

**Sakshi Gupta**

Data Science & AI Enthusiast
Focused on building intelligent data-driven applications.

GitHub: https://github.com/SakshiGupta8170
