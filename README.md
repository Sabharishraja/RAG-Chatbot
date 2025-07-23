# 📄 DocChat: Local Document-Based RAG Chatbot
## 🚀 Project Overview

**DocChat** is a local RAG (Retrieval-Augmented Generation) chatbot that allows users to upload their own documents and ask natural language questions. The chatbot returns answers based strictly on the content of those documents — no internet, no APIs, no LangChain.

---

## 🧠 Key Features

- ✅ Document-based question answering
- ✅ Fully offline (ideal for secure environments)
- ✅ Vector search via Qdrant
- ✅ Open-source LLMs (Flan-T5, Mistral)
- ✅ Lightweight UI with Streamlit
- ✅ Handles PDFs, custom queries, and document source tracking

---

## 🗂️ How It Works

1. PDFs are loaded and split into chunks
2. Each chunk is embedded using `sentence-transformers`
3. Embeddings stored in Qdrant vector database
4. On query, relevant chunks are retrieved
5. A prompt is generated and passed to a local LLM (Flan-T5 or Mistral)
6. The model responds based on the retrieved context

---

## 🧪 Sample Questions

- "What is the client-server model?"
- "What are the stages of a data science project?"
- "What are the types of topologies in networking?"
- "What is accuracy in machine learning?"

---

## 🛠️ Technologies Used

- Python
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Qdrant (Vector DB)
- Hugging Face Transformers
- Streamlit
- PyMuPDF / PDFMiner
- Mistral-7B / Flan-T5

---

## 🖥️ How to Run (Local)

1. Clone the repo  
2. Install dependencies:
3. Place your PDFs in the `/documents` folder  
4. Run embedding script (if needed)  
5. Start the chatbot: