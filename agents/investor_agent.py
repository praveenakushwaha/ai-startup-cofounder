from llms.groq_llm import get_groq_llm
from prompts.investor_prompt import INVESTOR_PROMPT


def investor_agent(state):

    llm = get_groq_llm()

    prompt = INVESTOR_PROMPT.format(
        startup_idea=state["startup_idea"],
        market_analysis=state["market_analysis"][:100],
        competitor_analysis=state["competitor_analysis"][:100],
        finance_analysis=state["finance_analysis"][:100],
        risk_analysis=state["risk_analysis"][:100]
    )

    response = llm.invoke(prompt)

    state["investor_analysis"] = response.content

    print("✅ Investor Agent Completed")

    return state