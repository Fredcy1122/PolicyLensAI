from app.rag.retriever import retrieve


def search_policy_documents(
    question: str
):
    return retrieve(
        question,
        top_k=5
    )
