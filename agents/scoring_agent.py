import json

from llms.groq_llm import get_groq_llm
from prompts.scoring_prompt import SCORING_PROMPT


def scoring_agent(state):

    llm = get_groq_llm()

    prompt = SCORING_PROMPT.format(
        startup_idea=state["startup_idea"],

        market_analysis=state["market_analysis"][:200],

        competitor_analysis=state["competitor_analysis"][:200],

        finance_analysis=state["finance_analysis"][:200],

        risk_analysis=state["risk_analysis"][:200]
    )

    response = llm.invoke(prompt)

    print("\nSCORING RESPONSE")
    print(response.content)

    try:

        cleaned = response.content.strip()

        start = cleaned.find("{")

        end = cleaned.rfind("}")

        cleaned = cleaned[start:end+1]

        parsed_json = json.loads(cleaned)

    except Exception as e:

        print("\nJSON ERROR")
        print(e)

        parsed_json = {
            "market_score": 5,
            "competition_score": 5,
            "finance_score": 5,
            "risk_score": 5,
            "overall_score": 5
        }

    state["scores"] = parsed_json

    state["startup_score"] = parsed_json

    print("\nSTATE SCORES")
    print(state["scores"])

    print("✅ Scoring Agent Completed")

    return state