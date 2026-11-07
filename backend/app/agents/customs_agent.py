from app.agents.agent_notes import (
    AgentNotes
)


class CustomsAgent:

    def analyze(
        self,
        question: str
    ):
        return {
            "agent": "Customs Agent",
            "focus":
                AgentNotes.customs()
        }