from app.agents.agent_notes import (
    AgentNotes
)
from app.tools.customs_checklist import (
    generate_import_checklist
)
from app.agents.document_review_agent import (
    DocumentReviewAgent
)

from app.tools.customs_checklist import (
    generate_import_checklist
)


class CustomsAgent:

    def analyze(
        self,
        question: str
    ):
        if "checklist" in question.lower():

            result = generate_import_checklist(
                question
            )

            return {
                "agent":
                    "Customs Agent",

                "tool_used":
                    "Import Checklist",

                "answer":
                    "\n".join(
                        result["requirements"]
                    )
            }

        return {
            "agent":
                "Customs Agent",

            "focus":
                AgentNotes.customs()
        }
        
    def checklist(
        self,
        cargo_type: str
    ):
        return generate_import_checklist(
            cargo_type
        )
    def review_document(
        self,
        content: str
    ):
        reviewer = DocumentReviewAgent()

        return {
            "agent": "Customs Agent",
            "answer": reviewer.review(
                content,
                "customs compliance"
            )
        }