from app.rag.retriever import retrieve


def evaluate_retrieval(
    question,
    expected_document
):

    results = retrieve(
        question,
        top_k=5
    )

    metadata = results["metadatas"][0]

    titles = [
        item.get("title")
        for item in metadata
    ]

    return expected_document in titles