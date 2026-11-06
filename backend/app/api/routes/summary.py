from fastapi import APIRouter
from pydantic import BaseModel

from app.services.summary_service import (
    summarize_document,
)

router = APIRouter()


class SummaryRequest(BaseModel):
    title: str
    content: str


@router.post("/summary")
def generate_summary(
    payload: SummaryRequest,
):
    summary = summarize_document(
        payload.title,
        payload.content,
    )

    return {
        "summary": summary
    }