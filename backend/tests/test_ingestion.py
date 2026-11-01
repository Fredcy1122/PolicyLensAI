from app.ingestion.metadata_extractor import (
    build_document_metadata
)


def test_metadata():

    metadata = build_document_metadata(
        "data/raw/legislation/customs_act.pdf"
    )

    assert metadata["filename"] == "customs_act.pdf"