from app.services.llm_service import (
    generate_response
)


class DocumentReviewAgent:

    def review(
        self,
        content: str,
        perspective: str
    ):

        content = content[:4000]

        prompt = f"""
Review this document from a
{perspective} perspective.

Document:

{content}

Return markdown.

# Findings

# Risks

# Compliance Considerations

Use only document evidence.
"""

        return generate_response(
            f"You are a {perspective} specialist.",
            prompt
        )