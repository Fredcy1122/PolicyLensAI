from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.document_repository import (
    DocumentRepository,
)

router = APIRouter()

repo = DocumentRepository()


@router.get("/dashboard/stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):
    documents = repo.get_all(db)

    document_count = len(documents)

    return {
        "documents": document_count,
        "chunks": 0,
        "queries": 0,
        "accuracy": 0,
    }