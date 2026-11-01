# tests/test_database.py

import uuid

from app.db.database import SessionLocal
from app.db.models import Document


def test_document_creation():

    db = SessionLocal()

    test_id = f"TEST_{uuid.uuid4().hex}"

    document = Document(
        document_id=test_id,
        title="Test Document"
    )

    db.add(document)
    db.commit()

    saved = (
        db.query(Document)
        .filter(Document.document_id == test_id)
        .first()
    )

    assert saved is not None

    db.delete(saved)
    db.commit()

    db.close()