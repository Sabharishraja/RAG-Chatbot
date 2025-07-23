from rag_utils import load_all_documents, generate_chunked_data
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
import uuid
import os
from tqdm import tqdm

print("📂 Loading and chunking documents...")
raw_docs = load_all_documents("documents")
chunked_docs = generate_chunked_data(raw_docs)
print(f"✅ Loaded and chunked {len(chunked_docs)} total chunks.")

print("🔍 Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model loaded.")

print("🧠 Setting up Qdrant client...")
client = QdrantClient(path="data") 
collection_name = "document_chunks"

client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)
print("✅ Qdrant collection created.")

print("🚀 Generating embeddings and uploading to Qdrant...")
points = []
for chunk in tqdm(chunked_docs):
    embedding = model.encode(chunk["text"]).tolist()
    point = PointStruct(
        id=str(uuid.uuid4()),
        vector=embedding,
        payload={
            "filename": chunk["filename"],
            "page": chunk["page"],
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"]
        }
    )
    points.append(point)

client.upsert(collection_name=collection_name, points=points)
print(f"✅ Uploaded {len(points)} chunks to Qdrant.")
