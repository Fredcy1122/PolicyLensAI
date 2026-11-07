from app.services.llm_service import (
    generate_response
)


def summarize_document(
    document_title: str,
    content: str
):
    prompt = f"""
Document Title:

{document_title}

Document Content:

{content}

Create an executive policy briefing.

Return the response in markdown format.

Structure exactly as:

# Executive Summary

Provide a concise overview of the document.

# Key Objectives

List the main goals of the document.

# Key Provisions

Summarize important provisions, obligations,
requirements, rights, duties, or restrictions.

# Compliance Requirements

Highlight actions required for compliance.

# Financial Implications

Identify taxes, duties, fees, tariffs,
penalties, costs, or financial impact.

If none are stated, say so.

# Operational Impact

Describe impact on organizations,
business operations, logistics,
trade, customs, or government agencies.

# Risks

Identify compliance risks,
regulatory risks, or legal risks.

# Recommendations

Provide practical recommendations
for management.

Use only evidence from the document.
Do not invent information.
"""

    return generate_response(
        "You are a senior policy, customs, trade, and regulatory analyst.",
        prompt,
    )
