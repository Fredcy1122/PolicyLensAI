from app.services.llm_service import (
    generate_response
)


class ClassifierAgent:

    def classify(
        self,
        content: str
    ):

        content = content[:3000]

        prompt = f"""
Classify this document into ONE category.

Categories:

LEGAL
FINANCE
CUSTOMS
TRADE
POLICY
MULTI_DOMAIN

Document:

{content}

Return ONLY the category name.
"""

        result = generate_response(
            "You are a regulatory document classifier.",
            prompt
        )

        return result.strip().upper()