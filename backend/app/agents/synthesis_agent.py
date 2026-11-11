from app.services.llm_service import (
    generate_response
)


class SynthesisAgent:

    def combine(
        self,
        results: list
    ):

        findings = []

        agents = []

        for result in results:

            if (
                isinstance(result, dict)
                and "answer" in result
            ):
                findings.append(
                    result["answer"]
                )

            if (
                isinstance(result, dict)
                and "agent" in result
            ):
                agents.append(
                    result["agent"]
                )

        combined_findings = (
            "\n\n".join(findings)
        )

        prompt = f"""
Create a consolidated executive report
from these specialist reviews.

{combined_findings}

Return markdown.

# Executive Summary

# Key Findings

# Compliance Obligations

# Risk Areas

# Financial Impact

# Trade Impact

# Customs Impact

# Recommended Actions

# Executive Recommendations
"""

        final_answer = generate_response(
            "You are a senior regulatory intelligence analyst.",
            prompt
        )

        return {
            "answer": final_answer,
            "contributors": len(results),
            "participating_agents": agents,
            "collaboration": True
        }