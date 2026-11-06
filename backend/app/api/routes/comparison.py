from fastapi import APIRouter
from pydantic import BaseModel

from app.services.comparison_service import (
    compare_documents,
)

router = APIRouter()


class ComparisonRequest(BaseModel):
    document_a: str
    document_b: str


@router.post("/comparison")
def compare(
    payload: ComparisonRequest,
):
    result = compare_documents(
        payload.document_a,
        payload.document_b,
    )

    return {
        "comparison": result
    }