def calculate_import_cost(
    customs_value: float,
    duty_rate: float,
    vat_rate: float = 7.5
):
    duty = (
        customs_value *
        duty_rate / 100
    )

    vat = (
        (customs_value + duty)
        * vat_rate / 100
    )

    total = (
        customs_value +
        duty +
        vat
    )

    return {
        "customs_value":
            customs_value,
        "duty":
            round(duty, 2),
        "vat":
            round(vat, 2),
        "total":
            round(total, 2),
    }
