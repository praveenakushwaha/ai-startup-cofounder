from llms.groq_llm import get_groq_llm
from prompts.cto_prompt import CTO_PROMPT


def cto_agent(state):

    llm = get_groq_llm()

    prompt = CTO_PROMPT.format(
        startup_idea=state["startup_idea"],
        market_analysis=state["market_analysis"],
        competitor_analysis=state["competitor_analysis"]
    )

    response = llm.invoke(prompt)

    state["tech_architecture"] = response.content

    print("✅ CTO Agent Completed")

    return state