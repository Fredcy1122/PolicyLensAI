from app.agents.legal_agent import (
    LegalAgent
)

from app.agents.finance_agent import (
    FinanceAgent
)

from app.agents.trade_agent import (
    TradeAgent
)

from app.agents.customs_agent import (
    CustomsAgent
)


def select_agents(
    document_type: str
):

    mapping = {

        "LEGAL": [
            LegalAgent()
        ],

        "FINANCE": [
            FinanceAgent(),
            LegalAgent()
        ],

        "CUSTOMS": [
            CustomsAgent(),
            TradeAgent(),
            LegalAgent()
        ],

        "TRADE": [
            TradeAgent(),
            FinanceAgent()
        ],

        "POLICY": [
            LegalAgent(),
            TradeAgent()
        ],

        "MULTI_DOMAIN": [
            LegalAgent(),
            FinanceAgent(),
            TradeAgent(),
            CustomsAgent()
        ]
    }

    return mapping.get(
        document_type,
        [LegalAgent()]
    )