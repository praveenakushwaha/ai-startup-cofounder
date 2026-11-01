from llms.groq_llm import get_groq_llm
from prompts.report_prompt import REPORT_PROMPT


def final_report_agent(state):

    llm = get_groq_llm()

    prompt = REPORT_PROMPT.format(
        startup_idea=state["startup_idea"],
        market_analysis=state["market_analysis"][:100],
        competitor_analysis=state["competitor_analysis"][:100],
        tech_architecture=state["tech_architecture"][:100],
        finance_analysis=state["finance_analysis"][:100],
        risk_analysis=state["risk_analysis"][:100], 
        investor_analysis=state["investor_analysis"][:100],
        startup_score=str(state["startup_score"])
    )

    response = llm.invoke(prompt)

    state["final_report"] = response.content

    print("✅ Final Report Agent Completed")

    return state