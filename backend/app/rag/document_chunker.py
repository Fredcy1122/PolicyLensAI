from app.rag.chunker import chunk_text

MAX_CHUNKS = 500

def chunk_document(
    document_id,
    title,
    pages
):
    chunks = []

    chunk_number = 1

    for page in pages:

        page_chunks = chunk_text(
            page["text"]
        )

        for chunk in page_chunks:

            if len(chunks) >= MAX_CHUNKS:
                break


            chunks.append(
                {
                    "chunk_id":
                        f"{document_id}_{chunk_number}",

                    "document_id":
                        document_id,

                    "title":
                        title,

                    "page":
                        page["page"],

                    "text":
                        chunk
                }
            )
        if len(chunks) >= MAX_CHUNKS:
            break

            chunk_number += 1

    return chunks