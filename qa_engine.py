from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from transformers import pipeline

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

qdrant = QdrantClient(path="data")
collection_name = "document_chunks"

print("⏳ Loading LLM...")
llm = pipeline("text2text-generation", model="google/flan-t5-small")
print("✅ LLM loaded.")

score_threshold = 0.3  

def retrieve_chunks(query, top_k=3):
    query_vector = embed_model.encode(query).tolist()
    results = qdrant.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k,
        with_payload=True
    )
    filtered_results = [r for r in results if r.score >= score_threshold]
    return filtered_results

def generate_answer(query):
    top_chunks = retrieve_chunks(query, top_k=3)
    if not top_chunks:
        return "Sorry, I couldn’t find an answer in the documents."

    combined_context = "\n\n".join([chunk.payload["text"] for chunk in top_chunks])

    max_chars = 1500
    if len(combined_context) > max_chars:
        combined_context = combined_context[:max_chars]

    meta = "; ".join([
        f"{chunk.payload['filename']} (Page {chunk.payload['page']}, Chunk {chunk.payload['chunk_id']})"
        for chunk in top_chunks
    ])

    prompt = f"""You are a helpful assistant. Answer the user's question **only** using the information provided in the context. If the context does not contain the answer, say "I couldn't find that in the document."\n\n{combined_context}\n\nQuestion: {query}"""

    response = llm(prompt, max_new_tokens=128 )[0]["generated_text"]
    answer = response.strip()

    return f"{answer}\n\n📄 Source(s): {meta}"
