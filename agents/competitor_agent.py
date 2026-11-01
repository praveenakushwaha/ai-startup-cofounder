from llms.groq_llm import get_groq_llm
from tools.github_tool import search_github_projects
from prompts.competitor_prompt import COMPETITOR_PROMPT

from tools.duckduckgo_tool import search_competitors


def competitor_agent(state):

    llm = get_groq_llm()

    competitors = search_competitors(
        f"{state['startup_idea']} competitors"
    )

    github_projects = search_github_projects(
        state["startup_idea"]
    )


    prompt = COMPETITOR_PROMPT.format(
    startup_idea=state["startup_idea"],
    competitors="\n".join(competitors),
    github_projects="\n".join(github_projects)
    )

    response = llm.invoke(prompt)

    state["competitor_analysis"] = response.content

    print("✅ Competitor Agent Completed")

    print("\nGitHub Projects:")
    print(github_projects)

    return state