from app.agents.agent_notes import (
    AgentNotes
)
from app.tools.legal_lookup import (
    lookup_section
)
import re

class LegalAgent:

    def analyze(
        self,
        question: str
    ):
        match = re.search(
            r"section\s+(\d+)",
            question.lower()
        )

        if match:

            section = match.group(1)

            result = lookup_section(
                section
            )

            return {
                "agent":
                    "Legal Agent",

                "tool_used":
                    "Section Lookup",

                "answer":
                    result["message"]
            }

        return {
            "agent":
                "Legal Agent",

            "focus":
                AgentNotes.legal()
        }
    def section_lookup(
        self,
        section_number: str
    ):
        return lookup_section(
            section_number
        )