from app.agents.agent_notes import (
    AgentNotes
)


class TradeAgent:

    def analyze(
        self,
        question: str
    ):
        return {
            "agent": "Trade Agent",
            "focus":
                AgentNotes.trade()
        }