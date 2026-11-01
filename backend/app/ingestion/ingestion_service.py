# backend/app/ingestion/ingestion_service.py

from app.ingestion.pdf_extractor import (
    extract_pdf_text
)

from app.ingestion.text_cleaner import (
    clean_text
)

from app.ingestion.metadata_extractor import (
    build_document_metadata
)


def ingest_document(file_path):

    metadata = build_document_metadata(file_path)

    pages = extract_pdf_text(file_path)

    processed_pages = []

    for page in pages:

        processed_pages.append(
            {
                "page": page["page"],
                "text": clean_text(page["text"])
            }
        )

    return {
        "metadata": metadata,
        "pages": processed_pages
    }