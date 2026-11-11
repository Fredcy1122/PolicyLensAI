from app.services.llm_service import (
    generate_response
)
from app.rag.document_retriever import (
    get_document_content
)


def compare_documents(
    document_a: str,
    document_b: str
):

    document_a_content = (
        get_document_content(
            document_a
        )
    )

    document_b_content = (
        get_document_content(
            document_b
        )
    )

    if not document_a_content:
        return (
            f"Document {document_a} "
            "could not be retrieved."
        )

    if not document_b_content:
        return (
            f"Document {document_b} "
            "could not be retrieved."
        )

    document_a_content = document_a_content[:4000]

    document_b_content = document_b_content[:4000]

    prompt = f"""
Compare the two regulatory documents.

DOCUMENT A:

{document_a_content}

DOCUMENT B:

{document_b_content}

Return markdown.

# Executive Summary

# Similarities

# Key Differences

# Compliance Gaps

# Legal Risks

# Financial Impact

# Customs Impact

# Trade Impact

# Recommended Actions

Use only the evidence provided.
Do not invent information.
"""

    return generate_response(
        "You are a senior regulatory compliance analyst.",
        prompt
    )