import chromadb

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
