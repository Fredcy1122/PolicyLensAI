from app.rag.vector_store import (
    get_collection
)


def retrieve(
    query,
    top_k=3
):

    query_embedding = (
        generate_embedding(query)
    )

    results = get_collection().query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    return results