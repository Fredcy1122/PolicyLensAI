def generate_import_checklist(
    cargo_type: str
):
    checklist = [
        "Form M",
        "PAAR",
        "Customs Declaration",
        "Duty Payment Receipt",
        "Terminal Release",
    ]

    if "food" in cargo_type.lower():
        checklist.append(
            "NAFDAC Permit"
        )

    if "electronic" in cargo_type.lower():
        checklist.append(
            "SONCAP Certificate"
        )

    return {
        "cargo_type": cargo_type,
        "requirements": checklist
    }