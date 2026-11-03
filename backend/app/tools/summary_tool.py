from app.services.llm_service import (
    generate_response
)


def summarize_document(
    content: str
):

    prompt = f"""
Summarize this policy document.

CONTENT:

{content}
"""

    return generate_response(
        "You are a policy analyst.",
        prompt
    )

if intent == Intent.SUMMARY:

    return {
        "intent": intent,
        "message":
            "Summary workflow coming next."
    }