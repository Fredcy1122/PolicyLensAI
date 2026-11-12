import chromadb

from app.rag.embeddings import generate_embeddings


_collection = None


def get_collection():
    global _collection

    if _collection is None:
        client = chromadb.PersistentClient(path="./chroma_db")
        _collection = client.get_or_create_collection(
            name="policy_documents"
        )

    return _collection


def add_chunks(chunks):
    ids = []
    documents = []
    metadatas = []
    seen_ids = set()

    for chunk in chunks:
        text = chunk.get("text", "").strip()
        if not text:
            continue

        chunk_id = str(chunk["chunk_id"])
        if chunk_id in seen_ids:
            raise ValueError(
                f"Duplicate chunk ID generated before vector storage: {chunk_id}"
            )
        seen_ids.add(chunk_id)

        ids.append(chunk_id)
        documents.append(text)
        metadatas.append(
            {
                "document_id": str(chunk["document_id"]),
                "page": int(chunk["page"]),
                "title": str(chunk["title"])
            }
        )

    if not documents:
        raise ValueError("No valid chunks were generated.")

    # One Azure request per batch rather than one request per chunk.
    embeddings = generate_embeddings(documents)

    if len(embeddings) != len(documents):
        raise RuntimeError(
            "Embedding count does not match the number of document chunks."
        )

    # Upsert makes retries/re-uploads idempotent for the same chunk IDs.
    get_collection().upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


def delete_document_chunks(document_id: str):
    get_collection().delete(
        where={"document_id": str(document_id)}
    )
