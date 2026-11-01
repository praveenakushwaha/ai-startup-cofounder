from llms.groq_llm import get_groq_llm
from prompts.risk_prompt import RISK_PROMPT


def risk_agent(state):

    llm = get_groq_llm()

    prompt = RISK_PROMPT.format(
        startup_idea=state["startup_idea"],
        market_analysis=state["market_analysis"][:100],
        competitor_analysis=state["competitor_analysis"][:100]
    )

    response = llm.invoke(prompt)

    state["risk_analysis"] = response.content

    print("✅ Risk Agent Completed")

    return state