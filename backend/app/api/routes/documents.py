from fastapi import APIRouter

router = APIRouter()


@router.get("/documents")
def get_documents():
    return [
        {
            "document_id": "DOC001",
            "title": "Nigeria Customs Act",
            "category": "Legislation",
            "status": "Active"
        }
    ]