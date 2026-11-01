from llms.groq_llm import get_groq_llm
from prompts.finance_prompt import FINANCE_PROMPT


def finance_agent(state):

    llm = get_groq_llm()

    prompt = FINANCE_PROMPT.format(
        startup_idea=state["startup_idea"],
        # market_analysis=state["market_analysis"],
        # competitor_analysis=state["competitor_analysis"],
        # tech_architecture=state["tech_architecture"]
        market_analysis=state["market_analysis"][:100],

        competitor_analysis=state["competitor_analysis"][:100],

        tech_architecture=state["tech_architecture"][:100]
    )

    response = llm.invoke(prompt)

    state["finance_analysis"] = response.content

    print("✅ Finance Agent Completed")

    return state