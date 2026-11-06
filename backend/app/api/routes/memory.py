from fastapi import APIRouter

from app.agents.persistent_memory import (
    PersistentMemory
)

router = APIRouter()


@router.get("/memory")
def memory_history():

    memory = PersistentMemory()

    items = memory.recent(10)

    return [
        {
            "question": item.question,
            "answer": item.answer,
            "agents": item.agents
        }
        for item in items
    ]