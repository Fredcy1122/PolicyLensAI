from app.rag.vector_store import (
    get_collection
)


def retrieve(
    query,
    top_k=3
):

    results = get_collection().query(
        query_texts=[query],
        n_results=top_k
    )

    return results