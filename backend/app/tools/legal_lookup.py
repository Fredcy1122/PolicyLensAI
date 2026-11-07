def lookup_section(
    section_number: str
):
    return {
        "section":
            section_number,
        "message":
            f"Section {section_number} located. "
            "Use document search for full text."
    }