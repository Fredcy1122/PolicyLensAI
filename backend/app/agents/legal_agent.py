from app.agents.agent_notes import (
    AgentNotes
)


class LegalAgent:

    def analyze(
        self,
        question: str
    ):
        return {
            "agent": "Legal Agent",
            "focus":
                AgentNotes.legal()
        }