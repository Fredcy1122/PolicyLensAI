from app.ingestion.pdf_extractor import (
    extract_pdf_text
)

from app.rag.document_chunker import (
    chunk_document
)

pages = extract_pdf_text(
    "../data/raw/legislation/customs_act.pdf"
)

chunks = chunk_document(
    document_id="DOC001",
    title="Customs Act",
    pages=pages
)

print(f"Chunks Created: {len(chunks)}")

print("\nSample Chunk\n")

print(chunks[0])