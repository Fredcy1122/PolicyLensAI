from difflib import unified_diff


def compare_documents(
    document_a: str,
    document_b: str
):

    differences = unified_diff(
        document_a.splitlines(),
        document_b.splitlines(),
        lineterm=""
    )

    return "\n".join(
        differences
    )