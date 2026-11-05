from app.agents.policy_agent import PolicyAgent
from app.agents.intents import Intent

from app.services.rag_service import (
    answer_question
)

from app.core.logger import logger


def execute_question(
    question: str
):

    agent = PolicyAgent()

    intent = agent.classify_intent(
        question
    )

    logger.info(
        f"Intent selected: {intent}"
    )

    if intent == Intent.RETRIEVAL:

        result = answer_question(
            question
        )

        result["intent"] = intent

        return result

    if intent == Intent.SUMMARY:

        return {
            "intent": intent,
            "message":
                "Summary functionality active"
        }

    if intent == Intent.COMPARISON:

        return {
            "intent": intent,
            "message":
                "Comparison functionality active"
        }

    if intent == Intent.METADATA:

        return {
            "intent": intent,
            "message":
                "Metadata functionality active"
        }

    return {
        "intent": intent,
        "message":
            "Tool not implemented yet."
    }