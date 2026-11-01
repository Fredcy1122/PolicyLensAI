from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.document_repository import (
    DocumentRepository
)

router = APIRouter()

repo = DocumentRepository()


@router.get("/documents")
def get_documents(
    db: Session = Depends(get_db)
):
    documents = repo.get_all(db)

    return [
        {
            "document_id": doc.document_id,
            "title": doc.title,
            "category": doc.category,
            "status": doc.status
        }
        for doc in documents
    ]