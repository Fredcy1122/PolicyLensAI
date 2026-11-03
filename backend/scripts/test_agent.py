from app.agents.policy_agent import (
    PolicyAgent
)

agent = PolicyAgent()

print(
    agent.decide_tool(
        "What is the Nigeria Customs Service Act?"
    )
)

print(
    agent.decide_tool(
        "Compare these policies"
    )
)

print(
    agent.decide_tool(
        "Give me a summary"
    )
)