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


def _prepare_chunks(chunks):
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

    return ids, documents, metadatas


def _upsert_chunks(ids, documents, metadatas):
    # Generate all embeddings before changing the existing vector records.
    embeddings = generate_embeddings(documents)

    if len(embeddings) != len(documents):
        raise RuntimeError(
            "Embedding count does not match the number of document chunks."
        )

    get_collection().upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


def add_chunks(chunks):
    """Add or update chunks without removing other chunks for the document."""
    ids, documents, metadatas = _prepare_chunks(chunks)
    _upsert_chunks(ids, documents, metadatas)


def replace_document_chunks(chunks):
    """
    Replace a document's indexed chunks safely.

    New embeddings are generated and upserted before obsolete chunks are
    deleted. If embedding generation fails, the previous index is untouched.
    """
    ids, documents, metadatas = _prepare_chunks(chunks)

    document_ids = {metadata["document_id"] for metadata in metadatas}
    if len(document_ids) != 1:
        raise ValueError(
            "replace_document_chunks expects chunks from exactly one document."
        )

    document_id = next(iter(document_ids))

    # This must complete successfully before any old chunks are removed.
    _upsert_chunks(ids, documents, metadatas)

    collection = get_collection()
    existing = collection.get(
        where={"document_id": document_id}
    )
    existing_ids = set(existing.get("ids", []))
    current_ids = set(ids)
    obsolete_ids = list(existing_ids - current_ids)

    # Remove leftovers when a replacement document contains fewer chunks.
    # If cleanup fails, the new chunks remain available and a retry can clean up.
    if obsolete_ids:
        collection.delete(ids=obsolete_ids)


def delete_document_chunks(document_id: str):
    get_collection().delete(
        where={"document_id": str(document_id)}
    )
