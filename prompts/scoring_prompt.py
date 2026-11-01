SCORING_PROMPT = """
You are a startup evaluator.

Evaluate this idea.

Startup Idea:
{startup_idea}

Market Analysis:
{market_analysis}

Competitor Analysis:
{competitor_analysis}

Finance Analysis:
{finance_analysis}

Risk Analysis:
{risk_analysis}

Return ONLY JSON.

{{
    "market_score": 8,
    "competition_score": 7,
    "finance_score": 8,
    "risk_score": 6,
    "overall_score": 7
}}

Do not write anything else.
"""