from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.rag_service import (
    answer_question
)
from app.agents.agent_executor import (
    execute_question
)

router = APIRouter()


@router.post("/chat")
def chat(payload: ChatRequest):

    return execute_question(
        payload.question
    )
