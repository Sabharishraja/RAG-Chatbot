from qa_engine import generate_answer

while True:
    query = input("Ask a question (or 'exit'): ")
    if query.lower() == "exit":
        break
    answer = generate_answer(query)
    print("\n🧠 Answer:\n", answer)
