FINANCE_PROMPT = """
You are a startup finance advisor.

Based on the information below, provide a SHORT report.

Startup Idea:
{startup_idea}

Market Analysis:
{market_analysis}

Competitor Analysis:
{competitor_analysis}

Tech Architecture:
{tech_architecture}

Return only:

1. MVP Cost
2. Monthly Cost
3. Revenue Potential
4. Funding Needed

Maximum 200 words.
"""
