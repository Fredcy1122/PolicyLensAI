from app.agents.base_agent import (
    BaseAgent
)


class LegalAgent(BaseAgent):

    SYSTEM_CONTEXT = """
You are a legal and regulatory expert.

Prioritize:

- Acts
- Regulations
- Sections
- Penalties
- Offences

Provide answers with legal precision.
"""
