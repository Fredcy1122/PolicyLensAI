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

    embeddings = [
        generate_embedding(doc)
        for doc in documents
    ]
    get_collection().add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    for chunk in chunks:

        ids.append(
            chunk["chunk_id"]
        )

        documents.append(
            chunk["text"]
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

    get_collection().add(
        ids=ids,
        documents=documents,
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