from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.rag_service import (
    answer_question
)

router = APIRouter()


@router.post("/chat")
def chat(payload: ChatRequest):

    return answer_question(
        payload.question
    )
