from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)
from app.repositories.document_repository import (
    DocumentRepository
)
from app.ingestion.ingestion_service import (
    ingest_document
)
from app.services.document_analysis_service import (
    analyze_document
)
from app.rag.document_chunker import (
    chunk_document
)

from app.rag.vector_store import (
    add_chunks
)

import os
from sqlalchemy.orm import Session
from app.rag.vector_store import (
    add_chunks,
    delete_document_chunks
)
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

@router.get(
    "/documents/analyze/{document_id}"
)
def analyze(
    document_id: str
):
    try:

        analysis = (
            analyze_document(
                document_id
            )
        )

        return analysis

    except Exception as e:

        return {
            "analysis":
                "Document analysis is temporarily unavailable due to Azure OpenAI rate limits. Please try again later.",
            "error":
                str(e)
        }

@router.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    upload_dir = "uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    ingestion_result = (
        ingest_document(
            file_path
        )
    )

    metadata = (
        ingestion_result[
            "metadata"
        ]
    )
    document_id = metadata.get(
        "document_id",
        file.filename
    )

    title = metadata.get(
        "title",
        file.filename
    )

    chunks = chunk_document(
        document_id=document_id,
        title=title,
        pages=ingestion_result["pages"]
    )
    delete_document_chunks(
        document_id
    )
    add_chunks(chunks)

    document = repo.create(
        db,
        {
            "document_id":
                document_id,

            "title":
                title,

            "category":
                metadata.get(
                    "category",
                    "General"
                ),

            "issuing_authority":
                metadata.get(
                    "issuing_authority",
                    "Unknown"
                ),

            "source_url":
                "",

            "status":
                "READY"
        }
    )

    return {
        "message":
            "Document uploaded successfully",

        "document_id":
            document.document_id
    }