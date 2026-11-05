from app.services.comparison_service import (
    compare_documents
)


def compare_policy_documents(
    document_a,
    document_b
):
    return compare_documents(
        document_a,
        document_b
    )


