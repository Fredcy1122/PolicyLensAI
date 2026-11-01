import json
from pathlib import Path

from app.ingestion.pdf_extractor import extract_pdf_text
from app.rag.document_chunker import chunk_document

pages = extract_pdf_text(
    "../data/raw/legislation/customs_act.pdf"
)

chunks = chunk_document(
    document_id="DOC001",
    title="Nigeria Customs Service Act 2023",
    pages=pages
)

output_dir = Path("../data/chunks")
output_dir.mkdir(exist_ok=True)

with open(
    output_dir / "DOC001_chunks.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        chunks,
        f,
        ensure_ascii=False,
        indent=2
    )

print(
    f"Saved {len(chunks)} chunks."
)