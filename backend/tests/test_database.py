from app.db.database import SessionLocal
from app.db.models import Document


def test_document_creation():

    db = SessionLocal()

    document = Document(
        document_id="TEST001",
        title="Test Document"
    )

    db.add(document)
    db.commit()

    saved = (
        db.query(Document)
        .filter(
            Document.document_id == "TEST001"
        )
        .first()
    )

    assert saved is not None

    db.close()