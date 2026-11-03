from app.agents.policy_agent import PolicyAgent
from app.agents.intents import Intent

from app.services.rag_service import (
    answer_question
)
from app.core.logger import logger

logger.info(
    f"Intent selected: {intent}"
)

def execute_question(
    question: str
):

    agent = PolicyAgent()

    intent = agent.classify_intent(
        question
    )

    if intent == Intent.RETRIEVAL:

        result = answer_question(
            question
        )

        result["intent"] = intent

        return result

    return {
        "intent": intent,
        "message":
            "Tool not implemented yet."
    }