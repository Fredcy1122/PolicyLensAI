def validate_evidence(
    retrieval_result
):

    if not retrieval_result:
        return False

    try:

        documents = retrieval_result[
            "documents"
        ][0]

        if len(documents) == 0:
            return False

        return True

    except Exception:

        return False