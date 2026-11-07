from fastapi import APIRouter
from pydantic import BaseModel

from app.services.summary_service import (
    summarize_document,
)
from app.rag.document_retriever import (
    get_document_content
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
@router.get(
    "/summary/document/{document_id}"
)
def summary_by_document(
    document_id: str
):
    content = (
        get_document_content(
            document_id
        )
    )
    content = content[:12000]
    try:

        summary = summarize_document(
            document_title=document_id,
            content=content
        )

    except Exception as e:

        return {
            "summary":
                "Summary generation temporarily unavailable due to Azure OpenAI rate limits. Please try again in a few minutes.",
            "error": str(e)
        }

    return {
        "summary": summary
    }