from agents.market_agent import market_agent
from agents.competitor_agent import competitor_agent


state = {
    "startup_idea": "AI Recruitment SaaS",
    "market_analysis": "",
    "competitor_analysis": ""
}

state = market_agent(state)

state = competitor_agent(state)

print("\nMARKET ANALYSIS")
print("=" * 50)
print(state["market_analysis"])

print("\nCOMPETITOR ANALYSIS")
print("=" * 50)
print(state["competitor_analysis"])