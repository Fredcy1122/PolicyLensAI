from sqlalchemy.orm import Session

from app.db.models import Document


def get_document_metadata(
    db: Session,
    document_id: str
):

    return (
        db.query(Document)
        .filter(
            Document.document_id == document_id
        )
        .first()
    )