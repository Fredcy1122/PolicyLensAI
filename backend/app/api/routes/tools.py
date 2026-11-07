from fastapi import APIRouter

from app.tools.tax_calculator import (
    calculate_import_cost
)
from app.tools.customs_checklist import (
    generate_import_checklist
)

from app.tools.legal_lookup import (
    lookup_section
)

from app.tools.trade_impact import (
    analyze_trade_impact
)

router = APIRouter()


@router.get("/tools/import-cost")
def import_cost(
    customs_value: float,
    duty_rate: float
):
    return calculate_import_cost(
        customs_value,
        duty_rate
    )
@router.get("/tools/checklist")
def checklist(
    cargo_type: str
):
    return generate_import_checklist(
        cargo_type
    )


@router.get("/tools/legal-section")
def legal_section(
    section: str
):
    return lookup_section(
        section
    )


@router.get("/tools/trade-impact")
def trade_impact(
    policy: str
):
    return analyze_trade_impact(
        policy
    )