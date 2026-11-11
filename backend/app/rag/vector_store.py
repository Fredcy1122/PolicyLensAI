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

    for chunk in chunks:

        get_collection().add(
            ids=[chunk["chunk_id"]],
            documents=[chunk["text"]],
            metadatas=[
                {
                    "document_id":
                        chunk["document_id"],

                    "page":
                        chunk["page"],

                    "title":
                        chunk["title"]
                }
            ]
        )