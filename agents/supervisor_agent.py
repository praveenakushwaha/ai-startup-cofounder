from llms.groq_llm import get_groq_llm


def supervisor_agent(state):

    llm = get_groq_llm()

    prompt = f"""
    Startup Idea:

    {state['startup_idea']}

    Decide what analysis is needed.
    """

    response = llm.invoke(prompt)

    state["supervisor_decision"] = response.content

    print("✅ Supervisor Agent Completed")
    print(
    state["supervisor_decision"]
)


    return state