# backend/app/ingestion/metadata_extractor.py

from pathlib import Path


def build_document_metadata(file_path):

    path = Path(file_path)

    return {
        "filename": path.name,
        "document_type": path.parent.name
    }