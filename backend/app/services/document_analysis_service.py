from app.rag.document_retriever import (
    get_document_content
)

from app.services.llm_service import (
    generate_response
)


def analyze_document(
    document_id: str
):
    content = (
        get_document_content(
            document_id
        )
    )

    # Prevent token explosions
    content = content[:12000]

    prompt = f"""
Create an executive regulatory assessment.

Document:

{content}

Return markdown.

# Executive Summary

# Legal Impact

# Financial Impact

# Customs Impact

# Trade Impact

# Compliance Risks

# Recommended Actions

Use only document evidence.
Do not invent information.
"""

    analysis = generate_response(
        "You are a senior regulatory intelligence analyst.",
        prompt
    )

    return analysis