from app.services.llm_service import generate_response


def summarize_document(
    document_title: str,
    content: str
):

    prompt = f"""
Document Title:

{document_title}

Document Content:

{content}

Generate a structured policy summary.

Sections:

1. Purpose
2. Scope
3. Key Provisions
4. Responsibilities
5. Enforcement Provisions
6. Important Notes

Use evidence only from the document.
"""

    return generate_response(
        "You are an expert policy analyst.",
        prompt,
    )