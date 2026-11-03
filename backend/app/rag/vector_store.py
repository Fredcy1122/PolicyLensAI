import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="policy_documents"
)

def add_chunks(chunks):

    for chunk in chunks:

        collection.add(
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