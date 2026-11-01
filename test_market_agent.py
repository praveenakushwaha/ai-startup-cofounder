from agents.market_agent import market_agent

state = {
    "startup_idea": "AI Recruitment SaaS",
    "market_analysis": ""
}

result = market_agent(state)

print(result["market_analysis"])