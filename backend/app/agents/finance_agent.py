from app.agents.agent_notes import (
    AgentNotes
)


class FinanceAgent:

    def analyze(
        self,
        question: str
    ):
        return {
            "agent": "Finance Agent",
            "focus":
                AgentNotes.finance()
        }