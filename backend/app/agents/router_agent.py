from app.agents.intents import (
    Intent
)


class RouterAgent:

    def score_agents(
        self,
        question: str
    ):
        q = question.lower()

        scores = {
            Intent.LEGAL: 0,
            Intent.CUSTOMS: 0,
            Intent.TRADE: 0,
            Intent.FINANCE: 0,
            Intent.POLICY: 0,
        }

        matches = []

        legal_keywords = [
            "law",
            "act",
            "section",
            "offence",
            "penalty",
            "regulation",
        ]

        customs_keywords = [
            "customs",
            "port",
            "cargo",
            "clearance",
            "declaration",
            "import",
            "export",
        ]

        finance_keywords = [
            "tax",
            "vat",
            "duty",
            "levy",
            "tariff",
            "cost",
            "finance",
            "withholding",
        ]

        trade_keywords = [
            "trade",
            "agreement",
            "commerce",
            "treaty",
            "facilitation",
        ]

        for keyword in legal_keywords:
            if keyword in q:
                matches.append(keyword)
                scores[Intent.LEGAL] += 1

        for keyword in customs_keywords:
            if keyword in q:
                matches.append(keyword)
                scores[Intent.CUSTOMS] += 1

        for keyword in finance_keywords:
            if keyword in q:
                matches.append(keyword)
                scores[Intent.FINANCE] += 1

        for keyword in trade_keywords:
            if keyword in q:
                matches.append(keyword)
                scores[Intent.TRADE] += 1

        if max(scores.values()) == 0:
            scores[Intent.POLICY] = 1

        return {
            "rankings": sorted(
                scores.items(),
                key=lambda x: x[1],
                reverse=True,
            ),
            "matches": matches,
        }