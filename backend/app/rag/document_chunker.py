from app.rag.chunker import chunk_text


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

            chunk_number += 1

    return chunks