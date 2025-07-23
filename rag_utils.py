import fitz
import docx
import os

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    full_text = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        full_text.append({
            "text": page.get_text(),
            "page": page_num + 1
        })
    return full_text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return [{"text": para.text, "page": 1} for para in doc.paragraphs if para.text.strip()]

def load_all_documents(folder):
    all_chunks = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if filename.endswith(".pdf"):
            chunks = extract_text_from_pdf(path)
        elif filename.endswith(".docx"):
            chunks = extract_text_from_docx(path)
        else:
            continue
        for chunk in chunks:
            all_chunks.append({
                "filename": filename,
                "page": chunk["page"],
                "text": chunk["text"]
            })
    return all_chunks

def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

def generate_chunked_data(raw_docs):
    chunked_data = []
    for doc in raw_docs:
        chunks = chunk_text(doc['text'])
        for idx, chunk in enumerate(chunks):
            chunked_data.append({
                "text": chunk,
                "filename": doc["filename"],
                "page": doc["page"],
                "chunk_id": idx
            })
    return chunked_data
