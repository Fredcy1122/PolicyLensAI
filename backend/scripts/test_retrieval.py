from app.rag.retriever import retrieve

results = retrieve(
    "What is the Nigeria Customs Service Act?"
)

print(results)