import streamlit as st
from qa_engine import generate_answer

st.set_page_config(page_title="📄 DocChat - Local RAG Chatbot")

st.title("📄 DocChat: Ask Your Documents")
st.markdown("Ask a question and get answers from your uploaded PDFs!")

query = st.text_input("💬 Enter your question:")

if query:
    with st.spinner("🔍 Searching and generating answer..."):
        answer = generate_answer(query)
    st.markdown("### Answer:")
    st.success(answer)