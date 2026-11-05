from app.services.summary_service import (
    summarize_document
)


def generate_document_summary(
    title,
    content
):
    return summarize_document(
        title,
        content
    )