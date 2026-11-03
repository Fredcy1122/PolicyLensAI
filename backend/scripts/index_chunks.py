import json

from app.rag.vector_store import add_chunks

with open(
    "../data/chunks/DOC001_chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)

add_chunks(chunks)

print(
    f"Indexed {len(chunks)} chunks"
)