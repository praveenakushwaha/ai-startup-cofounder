from llms.groq_llm import get_groq_llm
from tools.trends_tool import get_trends
from tools.news_tool import get_startup_news
from prompts.market_prompt import MARKET_PROMPT

def market_agent(state):

    news = get_startup_news()

    print("\nNEWS DATA")
    print(news)


    llm = get_groq_llm()

    trends = get_trends(
        state["startup_idea"]
    )
    print("\nTRENDS DATA")
    print(trends)
    
    prompt = MARKET_PROMPT.format(
    startup_idea=state["startup_idea"],
    trends_data=str(trends),
    news="\n".join(news)
    )

    response = llm.invoke(prompt)

    state["market_analysis"] = response.content

    print("✅ Market Agent Completed")

    return state
