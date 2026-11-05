from app.rag.retriever import retrieve

from app.services.llm_service import (
    generate_response
)

from app.services.validation_service import (
    validate_evidence
)


def calculate_confidence(
    retrieval
):

    num_chunks = len(
        retrieval["documents"][0]
    )

    if num_chunks >= 5:
        return "HIGH"

    if num_chunks >= 3:
        return "MEDIUM"

    return "LOW"


SYSTEM_PROMPT = """
You are PolicyLens AI.

You are an evidence-grounded policy intelligence assistant.

Use ONLY the information supplied in the retrieved context.

Rules:

1. Never invent legislation.
2. Never invent policy requirements.
3. Never invent dates.
4. Never invent citations.
5. If evidence is insufficient, state that clearly.
6. Distinguish facts from interpretation.
7. Be concise and professional.
"""


def answer_question(question):

    retrieval = retrieve(
        question,
        top_k=5
    )

    if not validate_evidence(
        retrieval
    ):

        return {
            "answer":
                "Insufficient evidence found in the indexed documents.",
            "abstained": True,
            "citations": []
        }

    documents = retrieval["documents"][0]
    metadata = retrieval["metadatas"][0]

    confidence = calculate_confidence(
        retrieval
    )

    context_parts = []

    for doc, meta in zip(
        documents,
        metadata
    ):

        title = meta.get(
            "title",
            "Unknown Document"
        )

        page = meta.get(
            "page",
            "Unknown Page"
        )

        context_parts.append(
            f"""
SOURCE: {title}
PAGE: {page}

TEXT:
{doc}
"""
        )

    evidence = "\n\n".join(
        context_parts
    )

    prompt = f"""
QUESTION:

{question}

RETRIEVED EVIDENCE:

{evidence}

Answer the question and reference the
source document and page number when applicable.
"""

    answer = generate_response(
        SYSTEM_PROMPT,
        prompt
    )

    citations = []

    for meta in metadata:

        citations.append(
            {
                "title":
                    meta.get("title"),

                "page":
                    meta.get("page")
            }
        )

    return {
        "answer": answer,
        "confidence": confidence,
        "citations": citations,
        "abstained": False
    }