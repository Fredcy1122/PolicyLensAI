import re

from app.agents.agent_notes import (
    AgentNotes
)

from app.tools.tax_calculator import (
    calculate_import_cost
)

from app.agents.document_review_agent import (
    DocumentReviewAgent
)

class FinanceAgent:

    def analyze(
        self,
        question: str
    ):

        lower = question.lower()

        if (
            "duty" in lower
            and "%" in lower
        ):

            numbers = re.findall(
                r"\d+(?:\.\d+)?",
                question
            )

            if len(numbers) >= 2:

                customs_value = float(
                    numbers[0]
                )

                duty_rate = float(
                    numbers[1]
                )

                result = (
                    calculate_import_cost(
                        customs_value,
                        duty_rate
                    )
                )

                return {
                    "agent":
                        "Finance Agent",
                    "tool_used":
                        "Tax Calculator",
                    "answer":
                        f"""
                    Customs Value:
                    ₦{customs_value:,.2f}

                    Duty:
                    ₦{result['duty']:,.2f}

                    VAT:
                    ₦{result['vat']:,.2f}

                    Total Landed Cost:
                    ₦{result['total']:,.2f}
                    """
                }

        return {
            "agent":
                "Finance Agent",
            "focus":
                AgentNotes.finance()
        }
    def review_document(
        self,
        content: str
    ):
        reviewer = DocumentReviewAgent()

        return {
            "agent": "Finance Agent",
            "answer": reviewer.review(
                content,
                "financial and tax"
            )
        }