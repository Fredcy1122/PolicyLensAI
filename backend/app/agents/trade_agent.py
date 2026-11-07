from app.agents.agent_notes import (
    AgentNotes
)
from app.tools.trade_impact import (
    analyze_trade_impact
)

class TradeAgent:

    def analyze(
        self,
        question: str
    ):
        if (
            "impact" in question.lower()
        ):

            result = analyze_trade_impact(
                question
            )

            return {
                "agent":
                    "Trade Agent",

                "tool_used":
                    "Trade Impact",

                "answer":
                    str(result)
            }

        return {
            "agent":
                "Trade Agent",

                "focus":
                    AgentNotes.trade()
        }
    def policy_impact(
        self,
        policy_name: str
    ):
        return analyze_trade_impact(
            policy_name
        )