from app.agents.intents import (
    Intent
)


class PolicyAgent:

    def classify_intent(
        self,
        question: str
    ) -> Intent:

        q = question.lower()

        finance_keywords = [
            "tax",
            "vat",
            "levy",
            "tariff",
            "duty",
            "finance",
            "withholding",
            "cost",
        ]

        customs_keywords = [
            "customs",
            "import",
            "export",
            "cargo",
            "clearance",
            "declaration",
            "port",
        ]

        legal_keywords = [
            "law",
            "act",
            "section",
            "penalty",
            "offence",
            "regulation",
        ]

        trade_keywords = [
            "trade",
            "agreement",
            "facilitation",
            "commerce",
            "treaty",
        ]

        if any(
            keyword in q
            for keyword in finance_keywords
        ):
            return Intent.FINANCE

        if any(
            keyword in q
            for keyword in customs_keywords
        ):
            return Intent.CUSTOMS

        if any(
            keyword in q
            for keyword in legal_keywords
        ):
            return Intent.LEGAL

        if any(
            keyword in q
            for keyword in trade_keywords
        ):
            return Intent.TRADE

        return Intent.POLICY