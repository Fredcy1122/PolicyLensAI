from app.rag.vector_store import (
    get_collection
)


def get_document_content(
    document_id: str
):
    results = get_collection().get(
        where={
            "document_id":
                document_id
        }
    )

    documents = (
        results.get(
            "documents",
            []
        )
    )

    return "\n\n".join(
        documents
    )