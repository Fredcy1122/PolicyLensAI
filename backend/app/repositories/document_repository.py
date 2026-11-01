from sqlalchemy.orm import Session

from app.db.models import Document


class DocumentRepository:

    def get_all(self, db: Session):
        return db.query(Document).all()

    def create(
        self,
        db: Session,
        document_data: dict
    ):
        document = Document(**document_data)

        db.add(document)
        db.commit()
        db.refresh(document)

        return document