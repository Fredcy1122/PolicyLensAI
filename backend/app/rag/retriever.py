from app.rag.vector_store import (
    collection
)


def retrieve(
    query,
    top_k=5
):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results