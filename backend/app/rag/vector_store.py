import chromadb
from app.rag.embeddings import (
    generate_embedding
)


_collection = None


def get_collection():
    global _collection

    if _collection is None:
        client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        _collection = client.get_or_create_collection(
            name="policy_documents"
        )

    return _collection

def add_chunks(chunks):

    ids = []
    documents = []
    metadatas = []
    embeddings = []

    for chunk in chunks:

        text = (
            chunk.get(
                "text",
                ""
            ).strip()
        )

        if not text:
            continue

        ids.append(
            chunk["chunk_id"]
        )

        documents.append(
            text
        )

        metadatas.append(
            {
                "document_id":
                    chunk["document_id"],

                "page":
                    chunk["page"],

                "title":
                    chunk["title"]
            }
        )

        embeddings.append(
            generate_embedding(
                text
            )
        )

    if not documents:
        raise ValueError(
            "No valid chunks were generated."
        )

    get_collection().add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )
def delete_document_chunks(
    document_id: str
):

    get_collection().delete(
        where={
            "document_id":
                document_id
        }
    )
